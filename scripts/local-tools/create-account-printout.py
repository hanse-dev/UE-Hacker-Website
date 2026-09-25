#!/usr/bin/env python3
"""Legt einen Account auf der UE Hacker Website an und druckt die Zugangsdaten
auf einem MXW01-Thermodrucker aus. Läuft nur lokal, nie auf dem Server.

Setup: siehe scripts/local-tools/README.md
"""
import argparse
import getpass
import json
import os
import secrets
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VENDOR_MXW01 = SCRIPT_DIR / "vendor" / "mxw01" / "MXW01print.py"
VENV_PYTHON = SCRIPT_DIR / "venv" / "bin" / "python3"
LAST_ACCOUNT_FILE = SCRIPT_DIR / ".last-account.json"


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


def save_last_account(username: str, password: str, age_group: str, server_url_raw: str) -> None:
    LAST_ACCOUNT_FILE.write_text(json.dumps({
        "username": username,
        "password": password,
        "ageGroup": age_group,
        "serverUrlRaw": server_url_raw,
    }))


def load_last_account() -> dict:
    if not LAST_ACCOUNT_FILE.exists():
        sys.exit(f"Kein zuvor angelegter Account gefunden ({LAST_ACCOUNT_FILE} existiert nicht).")
    return json.loads(LAST_ACCOUNT_FILE.read_text())


def generate_password() -> str:
    word1, word2 = secrets.SystemRandom().sample(PASSWORD_WORDS, 2)
    digits = f"{secrets.randbelow(100):02d}"
    return f"{word1}-{word2}-{digits}"


def api_request(url: str, payload: dict, token: str | None = None) -> dict:
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(), headers=headers, method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        sys.exit(f"Fehler bei {url}: {e.code} {body}")


DEFAULT_RECEIPT_FONT_SCALE = 1.2


def build_receipt_image(username: str, password: str, server_url: str, font_scale: float) -> Path:
    from PIL import Image, ImageDraw, ImageFont

    width = 384
    margin = 14  # Abstand Rahmen zu Papierrand
    padding = 14  # Abstand Inhalt zu Rahmen
    inner_width = width - 2 * margin - 2 * padding
    domain = server_url.replace("https://", "").replace("http://", "").rstrip("/")

    def scaled(size: int) -> int:
        return round(size * font_scale)

    def font_path(bold: bool) -> str | None:
        try:
            from matplotlib import font_manager
            weight = "bold" if bold else "normal"
            props = font_manager.FontProperties(family="DejaVu Sans", weight=weight)
            return font_manager.findfont(props, fallback_to_default=True)
        except Exception:
            return None

    _font_paths = {False: font_path(False), True: font_path(True)}

    def font(size: int, bold: bool):
        path = _font_paths[bold]
        if path:
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                pass
        return ImageFont.load_default()

    def font_fit(text: str, size: int, bold: bool, max_width: int):
        """Verkleinert die Schrift schrittweise, falls der Text sonst über den Rahmen hinausragen würde
        (z.B. bei einem langen Benutzernamen)."""
        f = font(size, bold)
        scratch_draw = ImageDraw.Draw(Image.new("L", (1, 1)))
        while size > 10:
            bbox = scratch_draw.textbbox((0, 0), text, font=f)
            if bbox[2] - bbox[0] <= max_width:
                break
            size -= 2
            f = font(size, bold)
        return f

    # (Text, Schriftgröße, fett, zentriert) — Reihenfolge der Zeilen im Rahmen
    rows = [
        ("UE HACKER", scaled(26), True, True),
        ("Zugangsausweis", scaled(16), False, True),
        ("RULE", 0, False, False),  # Trennlinie, kein Text
        ("Name", scaled(14), False, False),
        (username, scaled(24), False, False),
        ("", scaled(6), False, False),
        ("Passwort", scaled(14), False, False),
        (password, scaled(24), False, False),
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

    out_path = Path(tempfile.mkstemp(suffix=".png")[1])
    img.save(out_path)
    return out_path


def print_receipt(image_path: Path, printer_address: str) -> None:
    if not VENDOR_MXW01.exists():
        sys.exit(
            f"MXW01-Tool fehlt unter {VENDOR_MXW01}.\n"
            f"Erst ausführen: {SCRIPT_DIR / 'setup-printer-tool.sh'}"
        )
    subprocess.run(
        [sys.executable, str(VENDOR_MXW01), "-i", str(image_path), "-d", printer_address],
        check=True,
    )


def main() -> None:
    reexec_in_venv()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("username", nargs="?", help="Gewünschter Benutzername (2-40 Zeichen, a-z/A-Z/0-9/._-)")
    parser.add_argument("age_group", nargs="?", choices=["kinder", "jugendliche"], help="Altersgruppe")
    parser.add_argument("--server-url", help="Überschreibt ACCOUNT_SERVER_URL aus .env")
    parser.add_argument("--printer-address", help="Überschreibt MXW01_PRINTER_ADDRESS aus .env")
    parser.add_argument("--no-print", action="store_true", help="Nur Account anlegen, nicht drucken")
    parser.add_argument(
        "--reprint", action="store_true",
        help="Zuletzt angelegten Account erneut drucken (kein neuer Account, keine username/age_group nötig) — z.B. wenn der Druck vorher fehlgeschlagen ist",
    )
    args = parser.parse_args()

    env = load_env_file(SCRIPT_DIR / ".env")
    server_url_raw = (args.server_url or env.get("ACCOUNT_SERVER_URL") or "").rstrip("/")
    printer_address = args.printer_address or env.get("MXW01_PRINTER_ADDRESS")
    try:
        font_scale = float(env.get("RECEIPT_FONT_SCALE") or DEFAULT_RECEIPT_FONT_SCALE)
    except ValueError:
        sys.exit(f"RECEIPT_FONT_SCALE in .env ist keine Zahl: {env.get('RECEIPT_FONT_SCALE')!r}")

    if args.reprint:
        account = load_last_account()
        username = account["username"]
        password = account["password"]
        print(f"Drucke zuletzt angelegten Account erneut: '{username}'")
    else:
        if not args.username or not args.age_group:
            parser.error("username und age_group sind nötig (außer bei --reprint)")

        server_url = normalize_server_url(server_url_raw) if server_url_raw else ""
        if not server_url:
            sys.exit("ACCOUNT_SERVER_URL fehlt (in scripts/local-tools/.env setzen oder --server-url übergeben).")

        admin_password = env.get("ADMIN_PASSWORD") or getpass.getpass("Admin-Passwort der Website: ")
        username = args.username
        password = generate_password()

        login = api_request(f"{server_url}/api/admin/login", {"password": admin_password})
        token = login["token"]

        api_request(
            f"{server_url}/api/admin/users",
            {"username": username, "password": password, "ageGroup": args.age_group},
            token=token,
        )
        print(f"Account '{username}' angelegt. Passwort: {password}")
        # Vor dem Druckversuch speichern — falls der Druck fehlschlägt, kann man mit
        # --reprint denselben Account (ohne neue Account-Anlage) erneut drucken.
        save_last_account(username, password, args.age_group, server_url_raw)

    if args.no_print:
        return

    if not printer_address:
        sys.exit("MXW01_PRINTER_ADDRESS fehlt (in scripts/local-tools/.env setzen oder --printer-address übergeben).")

    image_path = build_receipt_image(username, password, server_url_raw, font_scale)
    try:
        print_receipt(image_path, printer_address)
    finally:
        image_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
