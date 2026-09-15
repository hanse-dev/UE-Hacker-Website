import random
import math

systeme = ["Kepler-9b", "Proxima-II", "Orion-5", "Nova-Prime"]

# Schritt 1: Koordinaten erzeugen
print("=== NAVIGATIONSKALKULATOR ===")
koordinaten = {}
for system in systeme:
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    koordinaten[system] = (x, y)
    print(f"  {system}: ({x}, {y})")

# Schritt 2: Entfernungen berechnen (Pythagoras von 0,0)
print("\nEntfernungen von der Heimatstation (0,0):")
entfernungen = {}
for system, (x, y) in koordinaten.items():
    entfernung = round(math.sqrt(x**2 + y**2), 1)
    entfernungen[system] = entfernung
    print(f"  {system}: {entfernung} Lichtjahre")

# Schritt 3: Optimaler Reiseplan (sortiert nach Entfernung)
print("\n=== OPTIMALER REISEPLAN ===")
reiseplan = sorted(entfernungen.items(), key=lambda x: x[1])
for i, (system, entfernung) in enumerate(reiseplan, 1):
    print(f"  {i}. {system}: {entfernung} Lichtjahre")

# Bonus: Lichttage der längsten Reise
laengste = reiseplan[-1]
lichttage = round(laengste[1] / 10, 1)
print(f"\nBonus: Längste Reise ({laengste[0]}): {lichttage} Lichttage")