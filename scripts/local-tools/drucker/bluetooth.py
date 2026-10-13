"""Listet BLE-Geräte in Reichweite — hilft die Drucker-Adresse für MXW01_PRINTER_ADDRESS zu finden.

Auf macOS liefert CoreBluetooth keine echte Bluetooth-MAC-Adresse, sondern eine
zufällige, app-spezifische UUID (z.B. A652E1F0-...). Genau dieser Wert (nicht die
"echte" MAC von der Drucker-Verpackung/App) muss in .env als MXW01_PRINTER_ADDRESS
stehen. Auf Linux/Windows ist es dagegen die echte MAC-Adresse (XX:XX:XX:XX:XX:XX).
"""
import asyncio

DEFAULT_SCAN_SECONDS = 8.0


def scan(timeout: float = DEFAULT_SCAN_SECONDS) -> list[dict]:
    """Liefert die gefundenen Geräte als {address, name, is_printer}. Der Drucker muss an/wach sein."""
    async def discover():
        from bleak import BleakScanner

        return await BleakScanner.discover(timeout=timeout)

    return [
        {
            "address": d.address,
            "name": d.name,
            "is_printer": bool(d.name and "MXW01" in d.name.upper().replace(" ", "")),
        }
        for d in asyncio.run(discover())
    ]
