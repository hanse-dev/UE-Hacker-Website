# 🔍 Übungen mit return

# Beispiel 1: Einfache Berechnung mit return
def berechne_schaden(basis_schaden, multiplikator):
    """Berechnet den Gesamtschaden eines Angriffs"""
    gesamtschaden = basis_schaden * multiplikator
    return gesamtschaden

# Ergebnis in Variable speichern
print("=== Schadensberechnung ===")
schaden1 = berechne_schaden(10, 2)
print(f"Schlag 1: {schaden1} Schaden")

schaden2 = berechne_schaden(15, 3)
print(f"Schlag 2: {schaden2} Schaden")

# Ergebnis direkt verwenden
print(f"Kritischer Treffer: {berechne_schaden(20, 5)} Schaden")