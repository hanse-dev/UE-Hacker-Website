import random

# Schritt 1-2: Zeit-Loop
spruenge = 0
jahr = 2024

while True:
    sprung = random.choice([-50, -20, -10, 10, 25, 100])
    jahr += sprung
    spruenge += 1
    print(f"Sprung {spruenge}: Jahr {jahr} (Sprung: {sprung:+d})")

    # Schritt 3: Bedingung prüfen
    if 1900 <= jahr <= 2100:
        print(f"Stabile Zeit gefunden! {spruenge} Sprünge benötigt.")
        break
    if spruenge >= 20:
        print("Zeit-Paradoxon zu stark! Abbruch.")
        break