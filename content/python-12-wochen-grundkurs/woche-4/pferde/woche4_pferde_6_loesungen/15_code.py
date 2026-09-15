import random

# Schritt 1 – Variablen
ausdauer = 100
runden = 0
max_ausdauer = ausdauer

print("=== AUSDAUER-TRAINING STARTET ===")
print(f"Start-Ausdauer: {ausdauer}")
print()

# Schritt 1 – Haupt-Trainingsschleife
while True:
    runden += 1

    # Schritt 2 – Ausdauer verbrauchen
    verbrauch = random.randint(3, 8)
    ausdauer -= verbrauch

    # Schritt 4 – Statusmeldung alle 5 Runden
    if runden % 5 == 0:
        print(f"Runde {runden}: Ausdauer = {ausdauer}")

    # Schritt 3 – Sofort abbrechen wenn Ausdauer < 10
    if ausdauer < 10:
        print(f"⚠️ Ausdauer kritisch in Runde {runden}! Training gestoppt.")
        break

    # Schritt 3 – Champion nach 50 Runden
    if runden >= 50:
        print(f"🏆 Champion! 50 Runden geschafft!")
        break

# Abschlusszusammenfassung
print()
print("=== TRAININGSBERICHT ===")
print(f"Gesamte Runden: {runden}")
print(f"Letzte Ausdauer: {ausdauer}")
if runden >= 50:
    print("Bewertung: CHAMPION-REITER 🏆")
elif runden >= 30:
    print("Bewertung: Sehr gute Ausdauer ⭐")
else:
    print("Bewertung: Weiter trainieren 💪")