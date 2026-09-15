# 🔍 Übungen mit math-Konstanten
import math

print("=== Mathematische Konstanten ===")
print(f"Pi (π): {math.pi}")
print(f"Eulersche Zahl (e): {math.e}")
print(f"Unendlich: {math.inf}")
print(f"Tau (2π): {math.tau}")

# Praktische Anwendung: Kreisberechnungen
radius = 10
umfang = 2 * math.pi * radius
flaeche = math.pi * radius ** 2
print(f"\nKreis mit r={radius}:")
print(f"  Umfang: {umfang:.2f}")
print(f"  Fläche: {flaeche:.2f}")