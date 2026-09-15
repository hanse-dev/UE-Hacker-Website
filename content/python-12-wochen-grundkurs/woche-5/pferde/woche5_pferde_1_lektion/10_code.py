# 🔍 Übungen mit return

# Beispiel 1: Einfache Berechnung mit return
def berechne_trainingszeit(einheiten, dauer_pro_einheit):
    """Berechnet die gesamte Trainingszeit"""
    gesamtzeit = einheiten * dauer_pro_einheit
    return gesamtzeit

# Ergebnis in Variable speichern
print("=== Trainingszeit-Berechnung ===")
zeit1 = berechne_trainingszeit(5, 15)
print(f"Training 1: {zeit1} Minuten")

zeit2 = berechne_trainingszeit(3, 20)
print(f"Training 2: {zeit2} Minuten")

# Ergebnis direkt verwenden
print(f"Intensivtraining: {berechne_trainingszeit(10, 30)} Minuten")