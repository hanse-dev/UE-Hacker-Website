# 🔍 Übungen mit return

# Beispiel 1: Einfache Berechnung mit return
def berechne_warp_distanz(warp_faktor, zeit):
    """Berechnet die zurückgelegte Distanz im Warp"""
    distanz = warp_faktor * zeit * 1000
    return distanz

# Ergebnis in Variable speichern
print("=== Warp-Distanz-Berechnung ===")
distanz1 = berechne_warp_distanz(5, 10)
print(f"Sprung 1: {distanz1} Lichtjahre")

distanz2 = berechne_warp_distanz(8, 15)
print(f"Sprung 2: {distanz2} Lichtjahre")

# Ergebnis direkt verwenden
print(f"Notfall-Sprung: {berechne_warp_distanz(10, 5)} Lichtjahre")