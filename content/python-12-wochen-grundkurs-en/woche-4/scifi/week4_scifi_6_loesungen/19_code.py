# 8x8 grid with nested lists
grid = [["."] * 8 for _ in range(8)]

# Chessboard pattern
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            grid[row][col] = "#"

# Place object
grid[3][4] = "X"

# Print grid
print("=== HOLODECK ===")
for row in grid:
    print(" ".join(row))
print(f"Object at: Row 3, Column 4")