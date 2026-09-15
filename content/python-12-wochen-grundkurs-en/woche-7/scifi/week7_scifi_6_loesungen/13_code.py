import math
import random

# Step 1: Circle calculation (shield generator)
radius = 50  # meters
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print("=== Shield Generator Calculation ===")
print(f"Radius:        {radius} m")
print(f"Circumference: {circumference:.2f} m")
print(f"Area:          {area:.2f} m²")

# Step 2: Random energy values
energy_values = [random.randint(1, 100) for _ in range(5)]
total = sum(energy_values)
print(f"\nEnergy readings: {energy_values}")
print(f"Total:           {total}")

# Step 3: Angle conversion
print("\nNavigation angles:")
for degrees in [90, 180, 270]:
    radians = math.radians(degrees)
    print(f"  {degrees}° = {radians:.4f} rad")

# Step 4: Square roots
print("\nSquare root calculations:")
for number in [4, 9, 16, 25]:
    print(f"  √{number} = {math.sqrt(number):.1f}")

# Bonus: Trigonometry
angle = math.radians(45)
print(f"\nBonus: sin(45°) = {math.sin(angle):.4f}, cos(45°) = {math.cos(angle):.4f}")