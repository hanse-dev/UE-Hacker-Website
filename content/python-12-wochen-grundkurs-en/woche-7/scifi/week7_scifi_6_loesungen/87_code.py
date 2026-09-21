field = []
for row in range(8):
    line = []
    for column in range(8):
        line.append(0)
    field.append(line)
piece = [0, 0]
goal = [7, 7]
moves = 0
while True:
    if piece == goal:
        break
    if piece[1] < 7:
        piece[1] += 1
    else:
        piece[0] += 1
    moves += 1
print(f"Moves: {moves}")
print(f"Goal reached: {piece == goal}")
