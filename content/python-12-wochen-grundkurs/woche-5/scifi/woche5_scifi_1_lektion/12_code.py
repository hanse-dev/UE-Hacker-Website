# Beispiel 3: Funktion ohne expliziten return (None)
def zeige_ausruestung():
    """Zeigt die Standard-Ausrüstung (gibt nichts zurück)"""
    print("Deine Ausrüstung:")
    print("  - Phaser")
    print("  - Tricorder")
    print("  - Kommunikator")
    # Kein return - gibt automatisch None zurück

print("=== Ausrüstung anzeigen ===")
ergebnis = zeige_ausruestung()
print(f"Rückgabewert: {ergebnis}")
print("Funktionen ohne return geben immer None zurück!")