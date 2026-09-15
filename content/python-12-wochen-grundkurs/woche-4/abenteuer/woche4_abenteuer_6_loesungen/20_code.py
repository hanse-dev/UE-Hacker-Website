# Schritt 1 – Zauberwelt-Grid aufbauen (8×8)
groesse = 8
grid = []
for zeile in range(groesse):
    reihe = []
    for spalte in range(groesse):
        reihe.append(".")
    grid.append(reihe)

# Schritt 2 – Magier und Ziel platzieren
magier_pos = [0, 0]  # [zeile, spalte]
ziel_pos = [7, 7]

grid[magier_pos[0]][magier_pos[1]] = "M"
grid[ziel_pos[0]][ziel_pos[1]] = "Z"

# Grid ausgeben
print("=== ZAUBERWELT ===")
for reihe in grid:
    print(" ".join(reihe))
print()

# Schritt 3 – Bewegung simulieren
zug = 0
while True:
    zug += 1
    # Alte Position leeren
    grid[magier_pos[0]][magier_pos[1]] = "."

    # Schritt nach rechts oder unten
    if magier_pos[1] < groesse - 1:
        magier_pos[1] += 1
    elif magier_pos[0] < groesse - 1:
        magier_pos[0] += 1

    # Schritt 4 – Zielerreichung prüfen
    if magier_pos == ziel_pos:
        grid[magier_pos[0]][magier_pos[1]] = "🏆"
        print(f"Zug {zug}: Magier auf ({magier_pos[0]}, {magier_pos[1]})")
        print("🎉 ZIEL ERREICHT! Der Magier hat das Ziel gefunden!")
        break
    else:
        grid[magier_pos[0]][magier_pos[1]] = "M"

    # Koordinate ausgeben (Bonus)
    spalten_buchstaben = "ABCDEFGH"
    koordinate = f"{spalten_buchstaben[magier_pos[1]]}{magier_pos[0] + 1}"
    print(f"Zug {zug}: Magier auf Feld {koordinate}")

    if zug >= 20:
        print("Simulation beendet.")
        break