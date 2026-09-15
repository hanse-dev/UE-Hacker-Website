# Beispiel 3: Funktion ohne expliziten return (None)
def zeige_inventar():
    """Zeigt das Inventar (gibt nichts zurück)"""
    print("Dein Inventar:")
    print("  - Schwert")
    print("  - Schild")
    print("  - Heiltrank")
    # Kein return - gibt automatisch None zurück

print("=== Inventar anzeigen ===")
ergebnis = zeige_inventar()
print(f"Rückgabewert: {ergebnis}")
print("Funktionen ohne return geben immer None zurück!")