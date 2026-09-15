# Example 2: Shield generator
print("=== Example 2: Shield Generator ===")
energy = 100
minute = 1

while energy > 20:
    consumption = 15
    energy -= consumption
    print(f"Minute {minute}: -{consumption} energy, remaining: {energy}%")
    minute += 1

print(f"\n⚠️ Shield critical after {minute-1} minutes!")
print("Recharge energy!")