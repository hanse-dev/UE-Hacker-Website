row = 0
column = 0
moves = 0
while row < 7:
    row += 1
    column += 1
    moves += 1
if row == 7 and column == 7:
    print(f"Goal reached after {moves} moves")
