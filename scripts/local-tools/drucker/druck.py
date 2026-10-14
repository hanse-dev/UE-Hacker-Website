"""Gemeinsames für alle Drucker-Aktionen: Pfade, .env, Schriften, Ausdrucke speichern,
auflisten und an den MXW01 schicken. Fragt nie selbst etwas ab und beendet nie das Programm —
Fehler kommen als DruckerError, damit Menü, Kommandozeile oder eine GUI sie selbst anzeigen können.
"""
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent
VENDOR_MXW01 = SCRIPT_DIR / "vendor" / "mxw01" / "MXW01print.py"
VENV_PYTHON = SCRIPT_DIR / "venv" / "bin" / "python3"
# Enthält Zugangsausweise mit Klartext-Passwort — gitignored, nie committen.
AUSDRUCKE_DIR = SCRIPT_DIR / "ausdrucke"

PAPER_WIDTH = 384


class DruckerError(Exception):
    """Ein Fehler, den die Person am Rechner beheben kann (Drucker aus, Einstellung fehlt, …)."""


def reexec_in_venv(script: str) -> None:
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
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), str(Path(script).resolve()), *sys.argv[1:]])


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
        raise DruckerError("MXW01_PRINTER_ADDRESS fehlt (in scripts/local-tools/drucker/.env setzen oder --printer-address übergeben).")
    if not VENDOR_MXW01.exists():
        raise DruckerError(
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
    return path


def send_to_printer(image_path: Path, printer_address: str | None) -> None:
    try:
        subprocess.run(
            [sys.executable, str(VENDOR_MXW01), "-i", str(image_path), "-d", require_printer(printer_address)],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise DruckerError(
            f"Druck fehlgeschlagen (Exit-Code {e.returncode}). Drucker an und in Reichweite? Papier eingelegt?\n"
            f"Das Bild ist gespeichert ({image_path.name}) und lässt sich über die gespeicherten Ausdrucke erneut drucken."
        )


def list_printouts() -> list[Path]:
    return sorted(AUSDRUCKE_DIR.glob("*.png"), reverse=True)


def describe_printout(path: Path) -> str:
    parts = path.stem.split("_", 2)
    if len(parts) == 3 and len(parts[1]) == 6 and parts[1].isdigit():
        return f"{parts[0]} {parts[1][:2]}:{parts[1][2:4]}  {parts[2].replace('_', ' ', 1)}"
    return path.stem
