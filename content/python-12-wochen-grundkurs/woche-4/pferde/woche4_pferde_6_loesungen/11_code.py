# Schritt 1 – Alle Pferdenummern 1 bis 20
print("=== Alle Pferdenummern ===")
for i in range(1, 21):
    print(f"Pferd: {i}")

# Schritt 2 – Nur gerade Nummern
print()
print("=== Gerade Pferdenummern ===")
for i in range(2, 21, 2):
    print(f"Gerade Pferd: {i}")

# Schritt 2 – Rückwärts 20 bis 1
print()
print("=== Rückwärts-Countdown ===")
for i in range(20, 0, -1):
    print(f"Pferd: {i}")

# Schritt 3 – Summe Trainingsstunden (jedes Pferd 1 Stunde)
trainingsstunden = 0
for i in range(1, 21):
    trainingsstunden += 1
print()
print(f"Gesamte Trainingsstunden für 20 Pferde: {trainingsstunden}h")

# Bonus – Trainingsplan-Tabelle
print()
print("=== Trainingsplan ===")
for i in range(1, 11):
    print(f"Pferd {i:2d} | Trainingseinheiten: {i * i}")