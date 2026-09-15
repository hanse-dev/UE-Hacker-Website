# Beispiel 1: Das Würfel-Orakel befragen
import random

print("=== Das Würfel-Orakel ===")
print(f"Wurf 1: {random.randint(1, 6)}")
print(f"Wurf 2: {random.randint(1, 6)}")
print(f"Kommazahl 0-1: {random.random():.3f}")
print(f"Kommazahl 10-20: {random.uniform(10, 20):.2f}")

# Mit Seed reproduzierbar
random.seed(42)
print(f"\nMit Seed 42: {random.randint(1, 100)}")
random.seed(42)
print(f"Mit Seed 42 (nochmal): {random.randint(1, 100)} (gleiches Ergebnis!)")
