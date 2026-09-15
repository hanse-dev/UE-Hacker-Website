import random

players = ["Merlin", "Aria", "Dragan"]
wins = {name: 0 for name in players}

print("=== DICE TOURNAMENT ===")

for round_number in range(1, 6):
    print(f"\nRound {round_number}:")
    rolls = {}
    for name in players:
        roll = random.randint(1, 6)
        rolls[name] = roll
        print(f"  {name} rolls: {roll}")

    best = max(rolls, key=rolls.get)
    wins[best] += 1
    print(f"  -> Winner: {best}!")

print("\n=== TOURNAMENT RESULT ===")
for name, count in wins.items():
    print(f"  {name}: {count} rounds won")
champion = max(wins, key=wins.get)
print(f"\nOverall champion: {champion}!")

# Bonus: magic die
print("\n=== BONUS: Magic Die Round (1-20) ===")
for name in players:
    magic_roll = random.randint(1, 20)
    print(f"  {name}: {magic_roll}")
