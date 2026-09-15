# Beispiel 2: Kapseln sind unveränderlich
trainings_status = ("Aktiv", "Stabil", "Gesund")
print(f"Trainings-Status: {trainings_status}")

# Zugriff funktioniert
print(f"Status: {trainings_status[0]}")

# Ändern funktioniert NICHT!
try:
    trainings_status[0] = "Inaktiv"
except TypeError as e:
    print(f"Fehler: {e}")

# Aber Kapseln in Listen können geändert werden
training = [
    ("Dressur", "Aktiv"),
    ("Springen", "Stabil"),
    ("Western", "Gesund")
]
training[1] = ("Springen", "Inaktiv")
print(f"\nTraining nach Änderung: {training}")