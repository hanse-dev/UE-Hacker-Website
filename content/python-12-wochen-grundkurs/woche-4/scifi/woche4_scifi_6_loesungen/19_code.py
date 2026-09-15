# 8x8 Grid mit verschachtelten Listen
grid = [["." for _ in range(8)] for _ in range(8)]

# Schachbrett-Muster
for zeile in range(8):
    for spalte in range(8):
        if (zeile + spalte) % 2 == 0:
            grid[zeile][spalte] = "#"

# Objekt platzieren
grid[3][4] = "X"

# Grid ausgeben
print("=== HOLODECK ===")
for zeile in grid:
    print(" ".join(zeile))
print(f"Objekt bei: Zeile 3, Spalte 4")