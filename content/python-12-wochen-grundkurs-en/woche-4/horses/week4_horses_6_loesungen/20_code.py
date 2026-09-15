# Step 1 – Build riding board (6×6)
size = 6
board = []
for row in range(size):
    line = []
    for col in range(size):
        line.append(".")
    board.append(line)

# Step 2 – Place horse
horse_pos = [0, 0]  # [row, col]
target_pos = [5, 5]

board[horse_pos[0]][horse_pos[1]] = "P"
board[target_pos[0]][target_pos[1]] = "Z"

# Print board
print("=== RIDING BOARD ===")
print("  A B C D E F")
for nr, line in enumerate(board):
    print(f"{nr + 1} " + " ".join(line))
print()

# Steps 3 & 4 – Simulate movement
move = 0
while True:
    move += 1
    board[horse_pos[0]][horse_pos[1]] = "."

    # Step 4 – Dressage figure: first right, then down
    if horse_pos[1] < size - 1:
        horse_pos[1] += 1
    elif horse_pos[0] < size - 1:
        horse_pos[0] += 1

    # Step 4 – Target reached?
    if horse_pos == target_pos:
        board[horse_pos[0]][horse_pos[1]] = "🏆"
        col_letters = "ABCDEF"
        coordinate = f"{col_letters[horse_pos[1]]}{horse_pos[0] + 1}"
        print(f"Move {move}: Horse on field {coordinate}")
        print("🎉 TARGET REACHED! Dressage completed!")
        break
    else:
        board[horse_pos[0]][horse_pos[1]] = "P"

    # Bonus – Print coordinates
    col_letters = "ABCDEF"
    coordinate = f"{col_letters[horse_pos[1]]}{horse_pos[0] + 1}"
    print(f"Move {move}: Horse on field {coordinate}")

    if move >= 15:
        break