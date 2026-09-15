import math
import random

# Schritt 1: Reitplatz-Berechnung
radius = 25  # Meter
umfang = 2 * math.pi * radius
flaeche = math.pi * radius ** 2
print("=== Reitplatz-Berechnungen ===")
print(f"Radius:  {radius} m")
print(f"Umfang:  {umfang:.2f} m")
print(f"Fläche:  {flaeche:.2f} m²")

# Schritt 2: Zufällige Futterrationen
futterrationen = [random.randint(1, 100) for _ in range(5)]
summe = sum(futterrationen)
print(f"\nFutterrationen: {futterrationen}")
print(f"Gesamt:         {summe}")

# Schritt 3: Winkel-Umrechnung
print("\nWinkel-Umrechnung:")
for grad in [90, 180, 270]:
    bogenmass = math.radians(grad)
    print(f"  {grad}° = {bogenmass:.4f} rad")

# Schritt 4: Wurzeln
print("\nWurzel-Ziehen:")
for zahl in [4, 9, 16, 25]:
    print(f"  √{zahl} = {math.sqrt(zahl):.1f}")

# Bonus: Trigonometrie
winkel = math.radians(45)
print(f"\nBonus: sin(45°) = {math.sin(winkel):.4f}, cos(45°) = {math.cos(winkel):.4f}")