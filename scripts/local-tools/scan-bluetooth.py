#!/usr/bin/env python3
"""Listet BLE-Geräte in Reichweite — hilft die Drucker-Adresse für MXW01_PRINTER_ADDRESS zu finden.

Auf macOS liefert CoreBluetooth keine echte Bluetooth-MAC-Adresse, sondern eine
zufällige, app-spezifische UUID (z.B. A652E1F0-...). Genau dieser Wert (nicht die
"echte" MAC von der Drucker-Verpackung/App) muss in .env als MXW01_PRINTER_ADDRESS
stehen. Auf Linux/Windows ist es dagegen die echte MAC-Adresse (XX:XX:XX:XX:XX:XX).
"""
import asyncio
import os
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VENV_PYTHON = SCRIPT_DIR / "venv" / "bin" / "python3"


def reexec_in_venv() -> None:
    if not VENV_PYTHON.exists():
        return
    if sys.prefix == str(VENV_PYTHON.parent.parent):
        return
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), str(Path(__file__).resolve()), *sys.argv[1:]])


async def scan(timeout: float) -> None:
    from bleak import BleakScanner

    print(f"Scanne {timeout:.0f} Sekunden nach BLE-Geräten (Drucker muss an/wach sein)...")
    devices = await BleakScanner.discover(timeout=timeout)
    if not devices:
        print("Keine BLE-Geräte gefunden.")
        return
    for d in devices:
        marker = "  <-- vermutlich der Drucker" if d.name and "MXW01" in d.name.upper().replace(" ", "") else ""
        print(f"{d.address}  {d.name}{marker}")


def main() -> None:
    reexec_in_venv()
    timeout = float(sys.argv[1]) if len(sys.argv) > 1 else 8.0
    asyncio.run(scan(timeout))


if __name__ == "__main__":
    main()
