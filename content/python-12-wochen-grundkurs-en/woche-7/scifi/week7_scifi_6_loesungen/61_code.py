import random

def find_winner(rolls):
    best = 0
    for i in range(len(rolls)):
        if rolls[i] > rolls[best]:
            best = i
    return best
wins = [0, 0, 0]
for round_number in range(5):
    rolls = []
    for player in range(3):
        rolls.append(random.randint(1, 6))
    wins[find_winner(rolls)] += 1
total = 0
for w in wins:
    total += w
print(f"Wins in total: {total}")
