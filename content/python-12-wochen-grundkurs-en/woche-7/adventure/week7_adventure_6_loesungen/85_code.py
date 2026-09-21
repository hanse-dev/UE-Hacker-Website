board = []
for row in range(8):
    line = []
    for column in range(8):
        if (row + column) % 2 == 0:
            line.append("#")
        else:
            line.append(".")
    board.append(line)
for row in range(2):
    print(" ".join(board[row]))
