#!/usr/bin/env python3
"""Alles rund um den MXW01-Thermodrucker in einem Skript. Läuft nur lokal, nie auf dem Server.

Ohne Argumente startet ein Menü. Mit Unterbefehl läuft genau eine Aktion:

  drucker.py account <benutzername>   Account anlegen oder, falls es ihn schon gibt, Passwort zurücksetzen
  drucker.py ausdrucke [DATEI]        gespeicherten Ausdruck auswählen und erneut drucken
  drucker.py tabelle [-n ANZAHL]      Forscher-Tabelle aus micro:bit-Stufe 8 drucken
  drucker.py scan [SEKUNDEN]          Drucker-Adresse per Bluetooth suchen

Jeder Ausdruck wird als Bild unter ausdrucke/ gespeichert.

Setup: siehe scripts/local-tools/README.md
"""
import argparse
import asyncio
import getpass
import json
import os
import re
import secrets
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VENDOR_MXW01 = SCRIPT_DIR / "vendor" / "mxw01" / "MXW01print.py"
VENV_PYTHON = SCRIPT_DIR / "venv" / "bin" / "python3"
# Enthält Zugangsausweise mit Klartext-Passwort — gitignored, nie committen.
AUSDRUCKE_DIR = SCRIPT_DIR / "ausdrucke"
LESSON_FILE = SCRIPT_DIR.parent.parent / "content" / "microbit-auto" / "lektion-09.md"

PAPER_WIDTH = 384
DEFAULT_RECEIPT_FONT_SCALE = 1.2
DEFAULT_TABLE_FONT_SCALE = 1.0
DEFAULT_SCAN_SECONDS = 8.0
MAX_LISTED_PRINTOUTS = 20


def reexec_in_venv() -> None:
    """Startet das Skript im venv (Pillow/bleak/matplotlib) neu, falls es gerade unter
    einem anderen Interpreter läuft — verhindert 'ModuleNotFoundError: PIL', egal ob
    mit python3 oder venv/bin/python3 aufgerufen.

    venv/bin/python3 ist meist nur ein Symlink auf den System-Interpreter — .resolve()
    würde also beide als identisch behandeln. sys.prefix zeigt dagegen zuverlässig auf
    den venv-Ordner, sobald man tatsächlich über venv/bin/python3 gestartet wurde."""
    if not VENV_PYTHON.exists():
        return
    if sys.prefix == str(VENV_PYTHON.parent.parent):
        return
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), str(Path(__file__).resolve()), *sys.argv[1:]])


# ---------------------------------------------------------------------------
# Gemeinsames: .env, Schriften, Ausdrucke speichern und drucken
# ---------------------------------------------------------------------------

def load_env_file(path: Path) -> dict:
    values = {}
    if not path.exists():
        return values
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        values[key.strip()] = value.strip()
    return values


_font_paths: dict = {}


def load_font(size: int, bold: bool = False):
    from PIL import ImageFont

    if bold not in _font_paths:
        try:
            from matplotlib import font_manager
            props = font_manager.FontProperties(family="DejaVu Sans", weight="bold" if bold else "normal")
            _font_paths[bold] = font_manager.findfont(props, fallback_to_default=True)
        except Exception:
            _font_paths[bold] = None
    if _font_paths[bold]:
        try:
            return ImageFont.truetype(_font_paths[bold], size)
        except OSError:
            pass
    return ImageFont.load_default()


def require_printer(printer_address: str | None) -> str:
    """Bricht ab, bevor etwas angelegt oder gerendert wird, wenn der Druck ohnehin scheitern würde."""
    if not printer_address:
        sys.exit("MXW01_PRINTER_ADDRESS fehlt (in scripts/local-tools/.env setzen oder --printer-address übergeben).")
    if not VENDOR_MXW01.exists():
        sys.exit(
            f"MXW01-Tool fehlt unter {VENDOR_MXW01}.\n"
            f"Erst ausführen: {SCRIPT_DIR / 'setup-printer-tool.sh'}"
        )
    return printer_address


def save_printout(img, name: str) -> Path:
    """Speichert jeden Ausdruck als Bild, damit er sich später auswählen und erneut drucken lässt.
    Der Zeitstempel vorn sorgt dafür, dass die Dateinamen nach Alter sortieren."""
    AUSDRUCKE_DIR.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    base = f"{stamp}_{re.sub(r'[^A-Za-z0-9._-]', '_', name)}"
    path = AUSDRUCKE_DIR / f"{base}.png"
    counter = 2
    while path.exists():  # zwei Ausdrucke in derselben Sekunde dürfen sich nicht überschreiben
        path = AUSDRUCKE_DIR / f"{base}-{counter}.png"
        counter += 1
    img.save(path)
    print(f"Ausdruck gespeichert: {path.relative_to(SCRIPT_DIR)}")
    return path


def send_to_printer(image_path: Path, printer_address: str | None) -> None:
    try:
        subprocess.run(
            [sys.executable, str(VENDOR_MXW01), "-i", str(image_path), "-d", require_printer(printer_address)],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        sys.exit(
            f"Druck fehlgeschlagen (Exit-Code {e.returncode}). Drucker an und in Reichweite? Papier eingelegt?\n"
            f"Das Bild ist gespeichert ({image_path.name}) und lässt sich über \"ausdrucke\" erneut drucken."
        )


def list_printouts() -> list[Path]:
    return sorted(AUSDRUCKE_DIR.glob("*.png"), reverse=True)


def describe_printout(path: Path) -> str:
    parts = path.stem.split("_", 2)
    if len(parts) == 3 and len(parts[1]) == 6 and parts[1].isdigit():
        return f"{parts[0]} {parts[1][:2]}:{parts[1][2:4]}  {parts[2].replace('_', ' ', 1)}"
    return path.stem


def print_saved(printer_address: str | None, name: str | None = None) -> None:
    """Druckt einen gespeicherten Ausdruck: per Dateiname oder per Auswahl aus der Liste (neueste zuerst)."""
    files = list_printouts()
    if not files:
        sys.exit(f"Noch keine gespeicherten Ausdrucke in {AUSDRUCKE_DIR}.")
    if name:
        chosen = next((f for f in files if f.name == Path(name).name), None)
        if not chosen:
            sys.exit(f"Kein gespeicherter Ausdruck mit dem Namen '{Path(name).name}'.")
    else:
        shown = files[:MAX_LISTED_PRINTOUTS]
        print("Gespeicherte Ausdrucke (neueste zuerst):")
        for number, path in enumerate(shown, 1):
            print(f"  {number:>2}  {describe_printout(path)}")
        if len(files) > len(shown):
            print(f"      … und {len(files) - len(shown)} ältere in {AUSDRUCKE_DIR}")
        answer = ask("Welchen drucken? (Nummer, leer = abbrechen)")
        if not answer:
            return
        if not answer.isdigit() or not 1 <= int(answer) <= len(shown):
            sys.exit(f"Abgebrochen: '{answer}' steht nicht in der Liste.")
        chosen = shown[int(answer) - 1]
    send_to_printer(chosen, printer_address)


# ---------------------------------------------------------------------------
# Account anlegen oder Passwort neu setzen + Zugangsausweis
# ---------------------------------------------------------------------------

# Kurze, eindeutige deutsche Wörter für Passwörter (keine Umlaute/ß, damit sie sich leicht
# abtippen lassen) — bewusst klein gehalten, nicht als vollständige Wortliste gedacht.
PASSWORD_WORDS = [
    "Apfel", "Baum", "Berg", "Blume", "Boot", "Brot", "Delfin", "Drache", "Ecke", "Elefant",
    "Feuer", "Fisch", "Fuchs", "Garten", "Gitarre", "Hafen", "Hase", "Held", "Herbst", "Himmel",
    "Honig", "Hund", "Hut", "Igel", "Insel", "Katze", "Keks", "Kiwi", "Koffer", "Komet",
    "Konig", "Kranich", "Kuchen", "Lampe", "Lowe", "Mantel", "Meer", "Mond", "Muschel", "Nebel",
    "Nudel", "Ozean", "Panda", "Pilz", "Planet", "Pirat", "Rakete", "Ritter", "Roboter", "Sand",
    "Schiff", "Schnee", "See", "Sommer", "Stern", "Sturm", "Tiger", "Traum", "Tunnel", "Turm",
    "Vogel", "Wald", "Wal", "Welle", "Wiese", "Wind", "Winter", "Wolke", "Zauber", "Ziege",
    "Zirkus", "Zug",
]


def normalize_server_url(url: str) -> str:
    """Kodiert einen Umlaut-Hostnamen (z.B. übergangshacker.de) als Punycode —
    sonst schickt urllib den Host-Header unkodiert und der Server kappt die Verbindung."""
    parts = urllib.parse.urlsplit(url)
    host = parts.hostname or ""
    try:
        ascii_host = host.encode("idna").decode("ascii")
    except UnicodeError:
        ascii_host = host
    if parts.port:
        ascii_netloc = f"{ascii_host}:{parts.port}"
    else:
        ascii_netloc = ascii_host
    return urllib.parse.urlunsplit((parts.scheme, ascii_netloc, parts.path, parts.query, parts.fragment))


def generate_password() -> str:
    word1, word2 = secrets.SystemRandom().sample(PASSWORD_WORDS, 2)
    digits = f"{secrets.randbelow(100):02d}"
    return f"{word1}-{word2}-{digits}"


def api_request(url: str, payload: dict | None = None, token: str | None = None,
                method: str = "POST") -> dict:
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        sys.exit(f"Fehler bei {url}: {e.code} {body}")
    except urllib.error.URLError as e:
        sys.exit(f"Server nicht erreichbar ({url}): {e.reason}")


def build_receipt_image(username: str, password: str, server_url: str, font_scale: float,
                        one_time: bool = False):
    from PIL import Image, ImageDraw

    width = PAPER_WIDTH
    margin = 14  # Abstand Rahmen zu Papierrand
    padding = 14  # Abstand Inhalt zu Rahmen
    inner_width = width - 2 * margin - 2 * padding
    domain = server_url.replace("https://", "").replace("http://", "").rstrip("/")

    def scaled(size: int) -> int:
        return round(size * font_scale)

    def font_fit(text: str, size: int, bold: bool, max_width: int):
        """Verkleinert die Schrift schrittweise, falls der Text sonst über den Rahmen hinausragen würde
        (z.B. bei einem langen Benutzernamen)."""
        f = load_font(size, bold)
        scratch_draw = ImageDraw.Draw(Image.new("L", (1, 1)))
        while size > 10:
            bbox = scratch_draw.textbbox((0, 0), text, font=f)
            if bbox[2] - bbox[0] <= max_width:
                break
            size -= 2
            f = load_font(size, bold)
        return f

    # (Text, Schriftgröße, fett, zentriert) — Reihenfolge der Zeilen im Rahmen
    rows = [
        ("UE HACKER", scaled(26), True, True),
        ("Zugangsausweis", scaled(16), False, True),
        ("RULE", 0, False, False),  # Trennlinie, kein Text
        ("Name", scaled(14), False, False),
        (username, scaled(24), False, False),
        ("", scaled(6), False, False),
        ("Einmal-Passwort" if one_time else "Passwort", scaled(14), False, False),
        (password, scaled(24), False, False),
        # Nach einem Reset muss beim ersten Login ein eigenes Passwort gewählt werden.
        *([("", scaled(6), False, False),
           ("Beim Login wählst du", scaled(13), False, False),
           ("ein neues Passwort.", scaled(13), False, False)] if one_time else []),
        ("RULE", 0, False, False),
        (domain, scaled(14), False, True),
        (date.today().isoformat(), scaled(12), False, True),
    ]

    scratch = Image.new("L", (width, 10))
    draw = ImageDraw.Draw(scratch)
    row_heights = []
    content_height = 0
    for text, size, bold, centered in rows:
        if text == "RULE":
            h = 16
        else:
            f = font_fit(text or " ", size, bold, inner_width)
            bbox = draw.textbbox((0, 0), text or " ", font=f)
            h = (bbox[3] - bbox[1]) + 8
        row_heights.append(h)
        content_height += h

    frame_top = margin
    frame_height = padding * 2 + content_height
    total_height = frame_top + frame_height + margin
    frame_left = margin
    frame_right = width - margin

    img = Image.new("L", (width, total_height), color=255)
    draw = ImageDraw.Draw(img)

    # Doppelter Rahmen, wie ein Ausweis/Badge
    draw.rectangle(
        [frame_left, frame_top, frame_right, frame_top + frame_height],
        outline=0, width=3,
    )
    draw.rectangle(
        [frame_left + 6, frame_top + 6, frame_right - 6, frame_top + frame_height - 6],
        outline=0, width=1,
    )

    y = frame_top + padding
    for (text, size, bold, centered), h in zip(rows, row_heights):
        if text == "RULE":
            line_y = y + h // 2
            draw.line(
                [frame_left + padding, line_y, frame_right - padding, line_y],
                fill=0, width=1,
            )
        elif text:
            f = font_fit(text, size, bold, inner_width)
            bbox = draw.textbbox((0, 0), text, font=f)
            text_w = bbox[2] - bbox[0]
            if centered:
                x = frame_left + padding + max(0, (inner_width - text_w) // 2)
            else:
                x = frame_left + padding
            draw.text((x, y), text, font=f, fill=0, stroke_width=1, stroke_fill=0)
        y += h

    return img


def receipt_font_scale(env: dict) -> float:
    try:
        return float(env.get("RECEIPT_FONT_SCALE") or DEFAULT_RECEIPT_FONT_SCALE)
    except ValueError:
        sys.exit(f"RECEIPT_FONT_SCALE in .env ist keine Zahl: {env.get('RECEIPT_FONT_SCALE')!r}")


def admin_session(env: dict, server_url_override: str | None, session: dict) -> dict:
    """Meldet sich als Admin an. `session` merkt sich das Token, damit das Menü nur einmal
    nach dem Admin-Passwort fragt."""
    if "token" not in session:
        server_url_raw = (server_url_override or env.get("ACCOUNT_SERVER_URL") or "").rstrip("/")
        server_url = normalize_server_url(server_url_raw) if server_url_raw else ""
        if not server_url:
            sys.exit("ACCOUNT_SERVER_URL fehlt (in scripts/local-tools/.env setzen oder --server-url übergeben).")
        admin_password = env.get("ADMIN_PASSWORD") or getpass.getpass("Admin-Passwort der Website: ")
        login = api_request(f"{server_url}/api/admin/login", {"password": admin_password})
        session.update(url=server_url, url_raw=server_url_raw, token=login["token"])
    return session


def set_account(
    username: str, env: dict, printer_address: str | None,
    age_group: str | None = None, reset: bool | None = None,
    server_url_override: str | None = None, no_print: bool = False, session: dict | None = None,
) -> None:
    """Legt den Account an oder setzt, falls es ihn schon gibt, auf Wunsch das Passwort zurück
    (Einmal-Passwort vom Server, beim nächsten Login muss ein eigenes gewählt werden).
    In beiden Fällen entsteht ein Zugangsausweis, der gespeichert und gedruckt wird.

    reset=None fragt nach, reset=True setzt ohne Rückfrage zurück. Fehlt age_group bei einem
    neuen Account, wird danach gefragt."""
    font_scale = receipt_font_scale(env)
    if not no_print:
        require_printer(printer_address)
    api = admin_session(env, server_url_override, {} if session is None else session)
    token = api["token"]

    users = api_request(f"{api['url']}/api/admin/users", token=token, method="GET")["users"]
    user = next((u for u in users if u["username"].lower() == username.lower()), None)
    kind = "account"

    if user:
        username = user["username"]
        if reset is None:
            reset = ask(f"Account '{username}' gibt es schon. Passwort zurücksetzen? (j/n)", "n").lower().startswith("j")
        if not reset:
            # Das alte Passwort lässt sich nicht auslesen — auf dem Server liegt nur ein Hash.
            print("Nichts geändert. Den früheren Zugangsausweis gibt es höchstens noch unter den gespeicherten Ausdrucken.")
            return
        # Der Server erzeugt das Einmal-Passwort selbst; das alte gilt ab jetzt nicht mehr und der
        # Account wird überall abgemeldet.
        result = api_request(f"{api['url']}/api/admin/users/{user['id']}/reset-password", {}, token=token)
        password = result["temporaryPassword"]
        print(f"Passwort von '{username}' zurückgesetzt. Einmal-Passwort: {password}")
        kind = "passwort-neu"
    else:
        if not age_group:
            choice = ask(f"Account '{username}' gibt es noch nicht. Altersgruppe: (k)inder oder (j)ugendliche", "k").lower()
            if choice not in ("k", "kinder", "j", "jugendliche"):
                sys.exit(f"Abgebrochen: unbekannte Altersgruppe '{choice}'.")
            age_group = "kinder" if choice.startswith("k") else "jugendliche"
        password = generate_password()
        api_request(
            f"{api['url']}/api/admin/users",
            {"username": username, "password": password, "ageGroup": age_group},
            token=token,
        )
        print(f"Account '{username}' angelegt. Passwort: {password}")

    # Erst speichern, dann drucken — schlägt der Druck fehl, bleibt der Ausweis erhalten.
    receipt = build_receipt_image(username, password, api["url_raw"], font_scale, one_time=bool(user))
    image_path = save_printout(receipt, f"{kind}_{username}")
    if not no_print:
        send_to_printer(image_path, printer_address)


# ---------------------------------------------------------------------------
# Forscher-Tabelle aus micro:bit-Stufe 8
# ---------------------------------------------------------------------------

def read_lesson_table(path: Path) -> tuple[str, list[str], list[list[str]]]:
    """Liefert Titel, Spaltenköpfe und Zeilen der ersten Markdown-Tabelle der Lektion."""
    title = ""
    table = []
    for line in path.read_text(encoding="utf8").splitlines():
        if line.startswith("# ") and not title:
            title = line[2:].strip()
        elif line.startswith("|"):
            table.append([cell.strip() for cell in line.strip().strip("|").split("|")])
        elif table:
            break
    if len(table) < 3:
        sys.exit(f"Keine Tabelle in {path} gefunden.")
    # table[1] ist die Trennzeile |---|---|
    return title, table[0], table[2:]


def build_table_image(title: str, header: list[str], rows: list[list[str]], font_scale: float, copies: int):
    from PIL import Image, ImageDraw

    margin = 10
    cell_pad = 8
    number_col = round(112 * font_scale)  # Spalte zum Eintragen der Zahl
    table_left = margin
    table_right = PAPER_WIDTH - margin
    split_x = table_right - number_col
    text_col = split_x - table_left - 2 * cell_pad

    def font(size: int, bold: bool = False):
        return load_font(round(size * font_scale), bold)

    scratch = ImageDraw.Draw(Image.new("L", (1, 1)))

    def wrap(text: str, f, max_width: int) -> list[str]:
        lines, current = [], ""
        for word in text.split():
            candidate = f"{current} {word}".strip()
            if current and scratch.textlength(candidate, font=f) > max_width:
                lines.append(current)
                current = word
            else:
                current = candidate
        return lines + [current] if current else lines

    def line_height(f) -> int:
        ascent, descent = f.getmetrics()
        return ascent + descent + 2

    title_font = font(22, bold=True)
    head_font = font(15, bold=True)
    body_font = font(17)
    small_font = font(14)

    footer = "Gut aufheben! In Stufe 9 baut ihr damit den Linienfolger."
    title_lines = wrap(title, title_font, PAPER_WIDTH - 2 * margin)
    footer_lines = wrap(footer, small_font, PAPER_WIDTH - 2 * margin)
    head_cells = [wrap(header[0], head_font, text_col), wrap(header[1], head_font, number_col - 2 * cell_pad)]
    body_cells = [wrap(row[0], body_font, text_col) for row in rows]
    # Mindesthöhe, damit eine handgeschriebene Zahl ins Feld passt
    min_row = round(64 * font_scale)

    def draw_copy(draw, y: int) -> int:
        """Zeichnet einen Ausdruck ab y und liefert das neue y. Mit draw=None wird nur gemessen."""
        y += margin
        for line in title_lines:
            if draw:
                draw.text((margin, y), line, font=title_font, fill=0)
            y += line_height(title_font)
        y += 6
        if draw:
            draw.text((margin, y), "Team:", font=small_font, fill=0)
            line_y = y + line_height(small_font) - 4
            draw.line([margin + 60 * font_scale, line_y, table_right, line_y], fill=0, width=1)
        y += line_height(small_font) + 12

        table_top = y
        head_h = max(len(cell) for cell in head_cells) * line_height(head_font) + 2 * cell_pad
        if draw:
            draw.rectangle([table_left, y, table_right, y + head_h], fill=0)
            for x, cell in ((table_left + cell_pad, head_cells[0]), (split_x + cell_pad, head_cells[1])):
                for i, line in enumerate(cell):
                    draw.text((x, y + cell_pad + i * line_height(head_font)), line, font=head_font, fill=255)
        y += head_h

        for cell in body_cells:
            text_h = len(cell) * line_height(body_font)
            row_h = max(min_row, text_h + 2 * cell_pad)
            if draw:
                text_y = y + (row_h - text_h) // 2
                for i, line in enumerate(cell):
                    draw.text((table_left + cell_pad, text_y + i * line_height(body_font)), line, font=body_font, fill=0)
                draw.line([table_left, y + row_h, table_right, y + row_h], fill=0, width=2)
            y += row_h

        if draw:
            draw.rectangle([table_left, table_top, table_right, y], outline=0, width=2)
            draw.line([split_x, table_top, split_x, y], fill=0, width=2)
        y += 10
        for line in footer_lines:
            if draw:
                draw.text((margin, y), line, font=small_font, fill=0)
            y += line_height(small_font)
        return y + margin

    copy_height = draw_copy(None, 0)
    cut_gap = 28  # Platz für die Schnittlinie zwischen zwei Ausdrucken
    total_height = copies * copy_height + (copies - 1) * cut_gap

    img = Image.new("L", (PAPER_WIDTH, total_height), color=255)
    draw = ImageDraw.Draw(img)
    y = 0
    for copy in range(copies):
        y = draw_copy(draw, y)
        if copy < copies - 1:
            for x in range(0, PAPER_WIDTH, 12):
                draw.line([x, y + cut_gap // 2, x + 6, y + cut_gap // 2], fill=0, width=1)
            y += cut_gap

    return img


def print_table(
    copies: int, printer_address: str | None,
    font_scale: float = DEFAULT_TABLE_FONT_SCALE, no_print: bool = False,
) -> None:
    if copies < 1:
        sys.exit("Die Anzahl muss mindestens 1 sein.")
    if not no_print:
        require_printer(printer_address)
    title, header, rows = read_lesson_table(LESSON_FILE)
    image_path = save_printout(build_table_image(title, header, rows, font_scale, copies), f"tabelle_{copies}x")
    if not no_print:
        send_to_printer(image_path, printer_address)


# ---------------------------------------------------------------------------
# Bluetooth-Scan
# ---------------------------------------------------------------------------

def scan_bluetooth(timeout: float = DEFAULT_SCAN_SECONDS) -> None:
    """Listet BLE-Geräte in Reichweite — hilft die Drucker-Adresse für MXW01_PRINTER_ADDRESS zu finden.

    Auf macOS liefert CoreBluetooth keine echte Bluetooth-MAC-Adresse, sondern eine
    zufällige, app-spezifische UUID (z.B. A652E1F0-...). Genau dieser Wert (nicht die
    "echte" MAC von der Drucker-Verpackung/App) muss in .env als MXW01_PRINTER_ADDRESS
    stehen. Auf Linux/Windows ist es dagegen die echte MAC-Adresse (XX:XX:XX:XX:XX:XX)."""
    async def scan() -> None:
        from bleak import BleakScanner

        print(f"Scanne {timeout:.0f} Sekunden nach BLE-Geräten (Drucker muss an/wach sein)...")
        devices = await BleakScanner.discover(timeout=timeout)
        if not devices:
            print("Keine BLE-Geräte gefunden.")
            return
        for d in devices:
            marker = "  <-- vermutlich der Drucker" if d.name and "MXW01" in d.name.upper().replace(" ", "") else ""
            print(f"{d.address}  {d.name}{marker}")

    asyncio.run(scan())


# ---------------------------------------------------------------------------
# Menü und Kommandozeile
# ---------------------------------------------------------------------------

MENU = """
UE Hacker – Thermodrucker
  1  Account: anlegen oder Passwort zurücksetzen
  2  Gespeicherten Ausdruck drucken
  3  Forscher-Tabelle drucken (micro:bit, Stufe 8)
  4  Drucker suchen (Bluetooth-Scan)
  0  Beenden"""


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    return input(f"{prompt}{suffix}: ").strip() or default


def menu_set_account(env: dict, printer_address: str | None, session: dict) -> None:
    username = ask("Benutzername")
    if not username:
        sys.exit("Abgebrochen: kein Benutzername.")
    set_account(username, env, printer_address, session=session)


def menu_print_table(printer_address: str | None) -> None:
    answer = ask("Wie viele Tabellen (eine pro Team)?", "1")
    if not answer.isdigit():
        sys.exit(f"Abgebrochen: '{answer}' ist keine Anzahl.")
    print_table(int(answer), printer_address)


def run_menu(env: dict, printer_address: str | None) -> None:
    session: dict = {}
    actions = {
        "1": lambda: menu_set_account(env, printer_address, session),
        "2": lambda: print_saved(printer_address),
        "3": lambda: menu_print_table(printer_address),
        "4": scan_bluetooth,
    }
    while True:
        print(MENU)
        try:
            choice = input("Auswahl: ").strip()
            if choice in ("0", "q", ""):
                return
            if choice not in actions:
                print(f"'{choice}' gibt es nicht.")
                continue
            actions[choice]()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        except SystemExit as e:
            # Ein Fehler in einer Aktion beendet nur die Aktion, nicht das Menü.
            if e.code not in (None, 0):
                print(e.code)


def main() -> None:
    reexec_in_venv()

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--printer-address", help="Überschreibt MXW01_PRINTER_ADDRESS aus .env")
    sub = parser.add_subparsers(dest="command", metavar="{account,ausdrucke,tabelle,scan}")

    p_account = sub.add_parser("account", help="Account anlegen oder, falls es ihn schon gibt, Passwort zurücksetzen (Einmal-Passwort)")
    p_account.add_argument("username", help="Benutzername (2-40 Zeichen, a-z/A-Z/0-9/._-)")
    p_account.add_argument("age_group", nargs="?", choices=["kinder", "jugendliche"], help="Altersgruppe für einen neuen Account (sonst wird gefragt)")
    p_account.add_argument("--reset", action="store_true", help="Passwort eines bestehenden Accounts ohne Rückfrage zurücksetzen")
    p_account.add_argument("--server-url", help="Überschreibt ACCOUNT_SERVER_URL aus .env")
    p_account.add_argument("--no-print", action="store_true", help="Ausweis nur speichern, nicht drucken")

    p_saved = sub.add_parser("ausdrucke", help="Gespeicherten Ausdruck auswählen und erneut drucken")
    p_saved.add_argument("datei", nargs="?", help="Dateiname aus ausdrucke/ (ohne Angabe: Liste zur Auswahl)")

    p_table = sub.add_parser("tabelle", help="Forscher-Tabelle aus micro:bit-Stufe 8 drucken")
    p_table.add_argument("-n", "--copies", type=int, default=1, help="Anzahl Tabellen, eine pro Team (Default 1)")
    p_table.add_argument("--font-scale", type=float, default=DEFAULT_TABLE_FONT_SCALE, help="Skaliert Schrift und Zeilenhöhe (Default 1.0)")
    p_table.add_argument("--no-print", action="store_true", help="Tabelle nur speichern, nicht drucken")

    p_scan = sub.add_parser("scan", help="Drucker-Adresse per Bluetooth suchen")
    p_scan.add_argument("seconds", nargs="?", type=float, default=DEFAULT_SCAN_SECONDS, help="Dauer des Scans (Default 8)")

    args = parser.parse_args()
    env = load_env_file(SCRIPT_DIR / ".env")
    printer_address = args.printer_address or env.get("MXW01_PRINTER_ADDRESS")

    if args.command == "account":
        set_account(
            args.username, env, printer_address,
            age_group=args.age_group, reset=True if args.reset else None,
            server_url_override=args.server_url, no_print=args.no_print,
        )
    elif args.command == "ausdrucke":
        print_saved(printer_address, args.datei)
    elif args.command == "tabelle":
        print_table(args.copies, printer_address, args.font_scale, args.no_print)
    elif args.command == "scan":
        scan_bluetooth(args.seconds)
    else:
        run_menu(env, printer_address)


if __name__ == "__main__":
    main()
