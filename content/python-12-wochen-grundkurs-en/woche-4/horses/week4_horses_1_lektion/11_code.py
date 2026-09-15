# Example 2: Horse training
print("=== Example 2: Training until exhaustion ===")
stamina = 100
round_ = 1

while stamina > 20:
    usage = 15
    stamina -= usage
    print(f"Round {round_}: -{usage} stamina, remaining: {stamina}%")
    round_ += 1

print(f"\n💪 Training finished after {round_-1} rounds!")
print("Time for a break!")