# Example 2: Game – Health and Energy
print("=== Example 2: Game Loop ===")
health = 100
round_ = 1

while health > 0:
    damage = 20
    health -= damage
    print(f"Round {round_}: -{damage} health, remaining: {health}")
    round_ += 1

print(f"\n💀 Game over after {round_-1} rounds!")