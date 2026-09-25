#!/usr/bin/env python3
"""Legt einen Account auf der UE Hacker Website an und druckt die Zugangsdaten
auf einem MXW01-Thermodrucker aus. Läuft nur lokal, nie auf dem Server.

Setup: siehe scripts/local-tools/README.md
"""
import argparse
import getpass
import json
import secrets
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VENDOR_MXW01 = SCRIPT_DIR / "vendor" / "mxw01" / "MXW01print.py"
PASSWORD_ALPHABET = "23456789ABCDEFGHJKMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz"  # ohne 0/O/1/l/I


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


def generate_password(length: int = 12) -> str:
    return "".join(secrets.choice(PASSWORD_ALPHABET) for _ in range(length))


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


def build_receipt_image(username: str, password: str, server_url: str) -> Path:
    from PIL import Image, ImageDraw, ImageFont

    width = 384
    domain = server_url.replace("https://", "").replace("http://", "").rstrip("/")
    lines = [
        ("UE Hacker Zugang", 28, True),
        ("", 10, False),
        ("Benutzername:", 18, False),
        (username, 26, True),
        ("", 8, False),
        ("Passwort:", 18, False),
        (password, 26, True),
        ("", 12, False),
        (domain, 16, False),
        (date.today().isoformat(), 14, False),
    ]

    def font(size: int, bold: bool):
        name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            return ImageFont.load_default()

    scratch = Image.new("L", (width, 10))
    draw = ImageDraw.Draw(scratch)
    row_heights = []
    total_height = 10
    for text, size, bold in lines:
        f = font(size, bold)
        bbox = draw.textbbox((0, 0), text or " ", font=f)
        h = (bbox[3] - bbox[1]) + 10
        row_heights.append(h)
        total_height += h

    img = Image.new("L", (width, total_height + 10), color=255)
    draw = ImageDraw.Draw(img)
    y = 10
    for (text, size, bold), h in zip(lines, row_heights):
        if text:
            f = font(size, bold)
            bbox = draw.textbbox((0, 0), text, font=f)
            text_w = bbox[2] - bbox[0]
            x = max(0, (width - text_w) // 2)
            draw.text((x, y), text, font=f, fill=0)
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("username", help="Gewünschter Benutzername (2-40 Zeichen, a-z/A-Z/0-9/._-)")
    parser.add_argument("age_group", choices=["kinder", "jugendliche"], help="Altersgruppe")
    parser.add_argument("--server-url", help="Überschreibt ACCOUNT_SERVER_URL aus .env")
    parser.add_argument("--printer-address", help="Überschreibt MXW01_PRINTER_ADDRESS aus .env")
    parser.add_argument("--no-print", action="store_true", help="Nur Account anlegen, nicht drucken")
    args = parser.parse_args()

    env = load_env_file(SCRIPT_DIR / ".env")
    server_url = (args.server_url or env.get("ACCOUNT_SERVER_URL") or "").rstrip("/")
    printer_address = args.printer_address or env.get("MXW01_PRINTER_ADDRESS")
    admin_password = env.get("ADMIN_PASSWORD") or getpass.getpass("Admin-Passwort der Website: ")

    if not server_url:
        sys.exit("ACCOUNT_SERVER_URL fehlt (in scripts/local-tools/.env setzen oder --server-url übergeben).")

    password = generate_password()

    login = api_request(f"{server_url}/api/admin/login", {"password": admin_password})
    token = login["token"]

    api_request(
        f"{server_url}/api/admin/users",
        {"username": args.username, "password": password, "ageGroup": args.age_group},
        token=token,
    )
    print(f"Account '{args.username}' angelegt. Passwort: {password}")

    if args.no_print:
        return

    if not printer_address:
        sys.exit("MXW01_PRINTER_ADDRESS fehlt (in scripts/local-tools/.env setzen oder --printer-address übergeben).")

    image_path = build_receipt_image(args.username, password, server_url)
    try:
        print_receipt(image_path, printer_address)
    finally:
        image_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
