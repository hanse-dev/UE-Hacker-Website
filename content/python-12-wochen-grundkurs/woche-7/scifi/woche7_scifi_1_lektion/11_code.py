# Beispiel 1: Zufallszahlen erzeugen
import random

print("=== Zufallszahlen ===")

# Ganzzahlen
print(f"Zufällige Zahl 1-6: {random.randint(1, 6)}")
print(f"Zufällige Zahl 0-100: {random.randint(0, 100)}")

# Kommazahlen
print(f"Zufallszahl 0-1: {random.random():.3f}")
print(f"Zufallszahl 10-20: {random.uniform(10, 20):.2f}")

# Mit Seeds reproduzierbar
random.seed(42)
print(f"Mit Seed 42: {random.randint(1, 100)}")
random.seed(42)
print(f"Mit Seed 42: {random.randint(1, 100)} (gleiches Ergebnis!)")