#!/usr/bin/env python3
"""Patcht vendor/mxw01/MXW01print.py: fügt eine kleine Pause zwischen den 20-Byte-
Häppchen beim Senden von Bild-/Feed-Daten ein.

Ohne Pause verwirft macOS (CoreBluetooth) reihenweise "write without response"-Pakete,
wenn sie zu schnell hintereinander gesendet werden — der Drucker bekommt dann nie ein
vollständiges Datenpaket, reagiert nicht (kein Papiervorschub, kein Druck) und sendet
auch keine Fehlermeldung zurück, nur ein stilles Timeout beim Warten auf die AA-Bestätigung.
Betrifft nur macOS; wird hier trotzdem plattformunabhängig angewendet, da die Pause
(10ms pro Häppchen) beim Drucken nicht spürbar ins Gewicht fällt.

Wird von setup-printer-tool.sh nach jedem frischen Klonen automatisch aufgerufen
(vendor/ ist gitignored, der Patch muss also bei jedem Setup neu angewendet werden).
Idempotent: prüft vorher, ob schon gepatcht wurde.
"""
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
TARGET = SCRIPT_DIR / "vendor" / "mxw01" / "MXW01print.py"

PATCHES = [
    (
        '''        max_chunk = 20 # Max bytes per write seems limited
        for j in range(0, len(printer_data), max_chunk):
            chunk = printer_data[j:j + max_chunk]
            await client.write_gatt_char(ae03_char.uuid, chunk, response=False)
        print("Finished sending image data.")''',
        '''        max_chunk = 20 # Max bytes per write seems limited
        for j in range(0, len(printer_data), max_chunk):
            chunk = printer_data[j:j + max_chunk]
            await client.write_gatt_char(ae03_char.uuid, chunk, response=False)
            await asyncio.sleep(0.01)  # macOS CoreBluetooth: ohne Pause verwirft es Writes stillschweigend
        print("Finished sending image data.")''',
    ),
    (
        '''            max_chunk = 20
            for j in range(0, len(blank_data), max_chunk):
                chunk = blank_data[j:j + max_chunk]
                await client.write_gatt_char(ae03_char.uuid, chunk, response=False)
            print("  Finished sending chunk blank data.")''',
        '''            max_chunk = 20
            for j in range(0, len(blank_data), max_chunk):
                chunk = blank_data[j:j + max_chunk]
                await client.write_gatt_char(ae03_char.uuid, chunk, response=False)
                await asyncio.sleep(0.01)  # macOS CoreBluetooth: ohne Pause verwirft es Writes stillschweigend
            print("  Finished sending chunk blank data.")''',
    ),
]


def main() -> None:
    if not TARGET.exists():
        sys.exit(f"{TARGET} fehlt — erst setup-printer-tool.sh laufen lassen.")

    src = TARGET.read_text()
    changed = False
    for old, new in PATCHES:
        if new in src:
            continue  # schon gepatcht
        if old not in src:
            print(f"Warnung: erwartete Stelle nicht gefunden in {TARGET.name} — Tool hat sich evtl. geändert, Patch übersprungen.")
            continue
        src = src.replace(old, new)
        changed = True

    if changed:
        TARGET.write_text(src)
        print("MXW01print.py gepatcht (Pause zwischen Daten-Häppchen für macOS).")
    else:
        print("MXW01print.py war schon gepatcht oder Patch nicht anwendbar.")


if __name__ == "__main__":
    main()
