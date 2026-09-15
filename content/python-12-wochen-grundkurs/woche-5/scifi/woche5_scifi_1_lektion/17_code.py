# ✨ Beispiele für gute und schlechte Namen

# ✅ Gute Namen (klar und beschreibend)
def berechne_schild_effizienz(energie, flaeche):
    """Berechnet die Effizienz der Schilde."""
    return (energie / flaeche) * 100

def finde_naechsten_hafen(schiff_position, hafen_liste):
    """Findet den nächsten Hafen zur aktuellen Position."""
    return min(hafen_liste, key=lambda h: abs(h - schiff_position))

def ist_kommunikation_moeglich(reichweite, distanz):
    """Prüft, ob Kommunikation möglich ist."""
    return distanz <= reichweite

# ❌ Schlechte Namen (unklar oder falsche Konvention)
# def berechneSchildEffizienz():  # CamelCase
# def se(e, f):  # Zu kurz, nicht beschreibend
# def shield_calculation():  # Substantiv zuerst

print("=== Gute Funktionsnamen in Aktion ===")
effizienz = berechne_schild_effizienz(1000, 50)
print(f"Schild-Effizienz: {effizienz}%")

position = 100
haefen = [50, 200, 350, 500]
naechster_hafen = finde_naechsten_hafen(position, haefen)
print(f"Nächster Hafen: {naechster_hafen}")

komm_ok = ist_kommunikation_moeglich(1000, 750)
print(f"Kommunikation möglich: {komm_ok}")