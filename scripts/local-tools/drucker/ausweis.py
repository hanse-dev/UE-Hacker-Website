"""Accounts auf der UE Hacker Website anlegen oder zurücksetzen (Admin-API) und den
Zugangsausweis dazu als Bild bauen. Fragt nie selbst etwas ab — siehe druck.py.
"""
import json
import secrets
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

from druck import PAPER_WIDTH, DruckerError, load_font, save_printout

DEFAULT_RECEIPT_FONT_SCALE = 1.2
AGE_GROUPS = ("kinder", "jugendliche")

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
        raise DruckerError(f"Fehler bei {url}: {e.code} {body}")
    except urllib.error.URLError as e:
        raise DruckerError(f"Server nicht erreichbar ({url}): {e.reason}")


def receipt_font_scale(env: dict) -> float:
    try:
        return float(env.get("RECEIPT_FONT_SCALE") or DEFAULT_RECEIPT_FONT_SCALE)
    except ValueError:
        raise DruckerError(f"RECEIPT_FONT_SCALE in .env ist keine Zahl: {env.get('RECEIPT_FONT_SCALE')!r}")


def needs_admin_password(env: dict) -> bool:
    return not env.get("ADMIN_PASSWORD")


def admin_login(env: dict, server_url_override: str | None = None, admin_password: str | None = None) -> dict:
    """Meldet sich als Admin an und liefert die Sitzung (url, url_raw, token). Das Admin-Passwort
    kommt aus .env oder vom Aufrufer (siehe needs_admin_password)."""
    server_url_raw = (server_url_override or env.get("ACCOUNT_SERVER_URL") or "").rstrip("/")
    server_url = normalize_server_url(server_url_raw) if server_url_raw else ""
    if not server_url:
        raise DruckerError("ACCOUNT_SERVER_URL fehlt (in scripts/local-tools/drucker/.env setzen oder --server-url übergeben).")
    password = env.get("ADMIN_PASSWORD") or admin_password
    if not password:
        raise DruckerError("Admin-Passwort fehlt.")
    login = api_request(f"{server_url}/api/admin/login", {"password": password})
    return {"url": server_url, "url_raw": server_url_raw, "token": login["token"]}


def find_user(session: dict, username: str) -> dict | None:
    """Sucht den Account (Groß-/Kleinschreibung egal). None, wenn es ihn noch nicht gibt."""
    users = api_request(f"{session['url']}/api/admin/users", token=session["token"], method="GET")["users"]
    return next((u for u in users if u["username"].lower() == username.lower()), None)


def create_user(session: dict, username: str, age_group: str) -> str:
    """Legt den Account mit einem Zufallspasswort an und liefert das Passwort."""
    if age_group not in AGE_GROUPS:
        raise DruckerError(f"Unbekannte Altersgruppe '{age_group}'.")
    password = generate_password()
    api_request(
        f"{session['url']}/api/admin/users",
        {"username": username, "password": password, "ageGroup": age_group},
        token=session["token"],
    )
    return password


def reset_password(session: dict, user: dict) -> str:
    """Lässt den Server ein Einmal-Passwort erzeugen und liefert es. Das alte Passwort gilt ab
    jetzt nicht mehr, der Account wird überall abgemeldet und muss beim nächsten Login ein eigenes
    Passwort wählen."""
    result = api_request(f"{session['url']}/api/admin/users/{user['id']}/reset-password", {}, token=session["token"])
    return result["temporaryPassword"]


def save_receipt(session: dict, username: str, password: str, font_scale: float, one_time: bool) -> Path:
    """Baut den Zugangsausweis und speichert ihn unter ausdrucke/. Drucken ist ein eigener Schritt."""
    receipt = build_receipt_image(username, password, session["url_raw"], font_scale, one_time=one_time)
    return save_printout(receipt, f"{'passwort-neu' if one_time else 'account'}_{username}")


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
