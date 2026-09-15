import random
import math

# Step 1: Planet selection
planets = ["Kepler-9b", "Proxima-II", "Orion-5", "Nova-Prime", "Cryon", "Aether-3"]
target_planet = random.choice(planets)
print("=== Nebula-7 Navigation System ===")
print(f"Known planets: {planets}")
print(f"Target planet: {target_planet}")

# Step 2: Weather simulation (temperatures of different sectors)
print("\nTemperature reading:")
sectors = ["Sector Alpha", "Sector Beta", "Sector Gamma"]
for sector in sectors:
    temperature = round(random.uniform(-50, 50), 1)
    print(f"  {sector}: {temperature}°C")

# Step 3: Energy consumption
print("\nSystem energy consumption:")
systems = ["Propulsion", "Shield Generator", "Life Support"]
total_energy = 0
for system in systems:
    consumption = random.randint(50, 150)
    total_energy += consumption
    print(f"  {system}: {consumption} MW")
print(f"  Total: {total_energy} MW")

# Step 4: Fleet generator
print("\nFleet ranking:")
ships = [(name, random.randint(1, 10)) for name in ["Nebula-7", "Star-Hawk", "Iron-Nova"]]
for name, strength in ships:
    print(f"  {name}: Combat power {strength}/10")

# Bonus: Gauss energy value
energy_gauss = round(random.gauss(100, 20), 1)
print(f"\nBonus – Gauss energy value: {energy_gauss} MW")