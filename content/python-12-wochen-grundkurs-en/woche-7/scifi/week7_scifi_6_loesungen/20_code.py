import random
import math

systems = ["Kepler-9b", "Proxima-II", "Orion-5", "Nova-Prime"]

# Step 1: Generate coordinates
print("=== NAVIGATION CALCULATOR ===")
coordinates = {}
for system in systems:
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    coordinates[system] = (x, y)
    print(f"  {system}: ({x}, {y})")

# Step 2: Calculate distances (Pythagoras from 0,0)
print("\nDistances from home station (0,0):")
distances = {}
for system, (x, y) in coordinates.items():
    distance = round(math.sqrt(x**2 + y**2), 1)
    distances[system] = distance
    print(f"  {system}: {distance} light-years")

# Step 3: Optimal travel plan (sorted by distance)
print("\n=== OPTIMAL TRAVEL PLAN ===")
travel_plan = sorted(distances.items(), key=lambda x: x[1])
for i, (system, distance) in enumerate(travel_plan, 1):
    print(f"  {i}. {system}: {distance} light-years")

# Bonus: Light-days for the longest journey
longest = travel_plan[-1]
light_days = round(longest[1] / 10, 1)
print(f"\nBonus: Longest journey ({longest[0]}): {light_days} light-days")