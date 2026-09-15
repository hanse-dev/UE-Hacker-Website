import random
import math

horses = ["Thunder", "Luna", "Blitz", "Silver", "Storm", "Cloud"]

# Step 1: Shuffle start list
random.shuffle(horses)
print("=== TOURNAMENT START LIST ===")
for i, horse in enumerate(horses, 1):
    print(f"  Start number {i}: {horse}")

# Step 2: Roll for performance
print("\nPerformance points:")
points = {horse: random.randint(1, 10) for horse in horses}
for horse, p in sorted(points.items(), key=lambda x: x[1], reverse=True):
    print(f"  {horse}: {p} points")

# Step 3: 3 tournament rounds
wins = {horse: 0 for horse in horses}
print("\n=== TOURNAMENT ROUNDS ===")
for round_num in range(1, 4):
    round_points = {horse: random.randint(1, 10) for horse in horses}
    winner = max(round_points, key=round_points.get)
    wins[winner] += 1
    print(f"Round {round_num}: {winner} wins!")

print("\n=== TOURNAMENT RESULT ===")
champion = max(wins, key=wins.get)
print(f"Tournament champion: {champion} ({wins[champion]} rounds)")

# Bonus: Minimum points for 60%
min_points = math.ceil(10 * 0.6)
print(f"\nBonus: Minimum points for 60% win chance: {min_points}")