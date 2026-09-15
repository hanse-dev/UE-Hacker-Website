import random
import math

# Schritt 1: Planetenauswahl
planeten = ["Kepler-9b", "Proxima-II", "Orion-5", "Nova-Prime", "Cryon", "Aether-3"]
zielplanet = random.choice(planeten)
print("=== Nebula-7 Navigationssystem ===")
print(f"Bekannte Planeten: {planeten}")
print(f"Zielplanet: {zielplanet}")

# Schritt 2: Wetter-Simulation (Temperaturen verschiedener Sektoren)
print("\nTemperatur-Messung:")
sektoren = ["Sektor Alpha", "Sektor Beta", "Sektor Gamma"]
for sektor in sektoren:
    temperatur = round(random.uniform(-50, 50), 1)
    print(f"  {sektor}: {temperatur}°C")

# Schritt 3: Energie-Verbrauch
print("\nEnergieverbrauch der Systeme:")
systeme = ["Antrieb", "Schildgenerator", "Lebenserhaltung"]
gesamt_energie = 0
for system in systeme:
    verbrauch = random.randint(50, 150)
    gesamt_energie += verbrauch
    print(f"  {system}: {verbrauch} MW")
print(f"  Gesamt: {gesamt_energie} MW")

# Schritt 4: Flotten-Generator
print("\nFlotten-Rangliste:")
schiffe = [(name, random.randint(1, 10)) for name in ["Nebula-7", "Star-Hawk", "Iron-Nova"]]
for name, staerke in schiffe:
    print(f"  {name}: Kampfkraft {staerke}/10")

# Bonus: Gauss-Energiewert
energie_gauss = round(random.gauss(100, 20), 1)
print(f"\nBonus – Gauss-Energiewert: {energie_gauss} MW")