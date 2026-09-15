# Beispiel 3: Fortgeschrittene Werkzeuge
import math

print("=== Fortgeschrittene Werkzeuge ===")

# Winkelfunktionen (in Bogenmaß!)
winkel_grad = 45
winkel_rad = math.radians(winkel_grad)
print(f"{winkel_grad}° = {winkel_rad:.3f} rad")
print(f"sin({winkel_grad}°): {math.sin(winkel_rad):.3f}")
print(f"cos({winkel_grad}°): {math.cos(winkel_rad):.3f}")
print(f"tan({winkel_grad}°): {math.tan(winkel_rad):.3f}")

# Logarithmen
print(f"\nlog(10): {math.log(10):.3f}")
print(f"log10(100): {math.log10(100)}")
print(f"log2(8): {math.log2(8)}")

# Spezielle Werkzeuge
print(f"\nfactorial(5): {math.factorial(5)}")
print(f"gcd(24, 36): {math.gcd(24, 36)}")
print(f"lcm(12, 15): {math.lcm(12, 15)}")