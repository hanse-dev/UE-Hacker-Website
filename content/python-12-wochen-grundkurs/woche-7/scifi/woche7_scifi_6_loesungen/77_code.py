ereignisse = ["Asteroid", "Sonnensturm", "Alien", "Nebel"]
import random

verlauf = []
for stockwerk in range(10):
    verlauf.append(random.choice(ereignisse))
alle_gueltig = True
for e in verlauf:
    if e not in ereignisse:
        alle_gueltig = False
print(f"Ereignisse: {len(verlauf)}")
print(f"Alle gültig: {alle_gueltig}")
