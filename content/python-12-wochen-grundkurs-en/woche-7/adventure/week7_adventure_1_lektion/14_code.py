# 🔍 Exercises with math constants
import math

print("=== Mathematical Constants ===")
print(f"Pi (π): {math.pi}")
print(f"Euler's number (e): {math.e}")
print(f"Infinity: {math.inf}")
print(f"Tau (2π): {math.tau}")

# Practical application: circle calculations
radius = 10
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"\nCircle with r={radius}:")
print(f"  Circumference: {circumference:.2f}")
print(f"  Area: {area:.2f}")