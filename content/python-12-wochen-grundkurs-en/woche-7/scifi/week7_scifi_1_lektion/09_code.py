# Example 3: Advanced math functions
import math

print("=== Advanced Functions ===")

# Trigonometric functions (in radians!)
angle_degrees = 45
angle_rad = math.radians(angle_degrees)
print(f"{angle_degrees}° = {angle_rad:.3f} rad")
print(f"sin({angle_degrees}°): {math.sin(angle_rad):.3f}")
print(f"cos({angle_degrees}°): {math.cos(angle_rad):.3f}")
print(f"tan({angle_degrees}°): {math.tan(angle_rad):.3f}")

# Logarithms
print(f"\nlog(10): {math.log(10):.3f}")
print(f"log10(100): {math.log10(100)}")
print(f"log2(8): {math.log2(8)}")

# Special functions
print(f"\nfactorial(5): {math.factorial(5)}")
print(f"gcd(24, 36): {math.gcd(24, 36)}")
print(f"lcm(12, 15): {math.lcm(12, 15)}")