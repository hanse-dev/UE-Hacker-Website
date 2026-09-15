# Beispiel 2: Aus Listen wählen
import random

print("=== Zufallsauswahl aus Listen ===")

# Planeten im System
planeten = ["Merkur", "Venus", "Erde", "Mars", "Jupiter", "Saturn"]
print(f"Alle Planeten: {planeten}")

# Ein zufälliger Planet
ziel = random.choice(planeten)
print(f"Zielplanet: {ziel}")

# Drei zufällige Planeten
flotte = random.choices(planeten, k=3)
print(f"Flottenziele: {flotte}")

# Liste mischen
reihenfolge = planeten.copy()
random.shuffle(reihenfolge)
print(f"Gemischte Reihenfolge: {reihenfolge}")