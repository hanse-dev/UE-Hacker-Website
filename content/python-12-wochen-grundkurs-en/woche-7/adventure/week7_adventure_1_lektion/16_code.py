# Example 3: Advanced tools
import math

print("=== Advanced Tools ===")

# Trigonometric functions (in radians!)
angle_deg = 45
angle_rad = math.radians(angle_deg)
print(f"{angle_deg}° = {angle_rad:.3f} rad")
print(f"sin({angle_deg}°): {math.sin(angle_rad):.3f}")
print(f"cos({angle_deg}°): {math.cos(angle_rad):.3f}")
print(f"tan({angle_deg}°): {math.tan(angle_rad):.3f}")

# Logarithms
print(f"\nlog(10): {math.log(10):.3f}")
print(f"log10(100): {math.log10(100)}")
print(f"log2(8): {math.log2(8)}")

# Special tools
print(f"\nfactorial(5): {math.factorial(5)}")
print(f"gcd(24, 36): {math.gcd(24, 36)}")
print(f"lcm(12, 15): {math.lcm(12, 15)}")