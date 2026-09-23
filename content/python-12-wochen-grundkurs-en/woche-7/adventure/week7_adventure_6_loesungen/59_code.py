def find_winner(rolls):
    best = 0
    for i in range(len(rolls)):
        if rolls[i] > rolls[best]:
            best = i
    return best

print(f"Winner: Player {find_winner([4, 6, 2]) + 1}")
