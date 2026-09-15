# Step 1 – Build enchanted world grid (8×8)
size = 8
grid = []
for row in range(size):
    line = []
    for col in range(size):
        line.append(".")
    grid.append(line)

# Step 2 – Place mage and goal
mage_pos = [0, 0]  # [row, col]
goal_pos = [7, 7]

grid[mage_pos[0]][mage_pos[1]] = "M"
grid[goal_pos[0]][goal_pos[1]] = "G"

# Print grid
print("=== ENCHANTED WORLD ===")
for line in grid:
    print(" ".join(line))
print()

# Step 3 – Simulate movement
move = 0
while True:
    move += 1
    # Clear old position
    grid[mage_pos[0]][mage_pos[1]] = "."

    # Step right or down
    if mage_pos[1] < size - 1:
        mage_pos[1] += 1
    elif mage_pos[0] < size - 1:
        mage_pos[0] += 1

    # Step 4 – Check if goal reached
    if mage_pos == goal_pos:
        grid[mage_pos[0]][mage_pos[1]] = "🏆"
        print(f"Move {move}: Mage at ({mage_pos[0]}, {mage_pos[1]})")
        print("🎉 GOAL REACHED! The mage has found the goal!")
        break
    else:
        grid[mage_pos[0]][mage_pos[1]] = "M"

    # Print coordinate (Bonus)
    col_letters = "ABCDEFGH"
    coordinate = f"{col_letters[mage_pos[1]]}{mage_pos[0] + 1}"
    print(f"Move {move}: Mage at square {coordinate}")

    if move >= 20:
        print("Simulation ended.")
        break