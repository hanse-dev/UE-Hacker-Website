# Schritt 1 – Reitbrett aufbauen (6×6)
groesse = 6
brett = []
for zeile in range(groesse):
    reihe = []
    for spalte in range(groesse):
        reihe.append(".")
    brett.append(reihe)

# Schritt 2 – Pferd platzieren
pferd_pos = [0, 0]  # [zeile, spalte]
ziel_pos = [5, 5]

brett[pferd_pos[0]][pferd_pos[1]] = "P"
brett[ziel_pos[0]][ziel_pos[1]] = "Z"

# Brett ausgeben
print("=== REITBRETT ===")
print("  A B C D E F")
for nr, reihe in enumerate(brett):
    print(f"{nr + 1} " + " ".join(reihe))
print()

# Schritt 3 & 4 – Bewegung simulieren
zug = 0
while True:
    zug += 1
    brett[pferd_pos[0]][pferd_pos[1]] = "."

    # Schritt 4 – Dressur-Figur: erst rechts, dann unten
    if pferd_pos[1] < groesse - 1:
        pferd_pos[1] += 1
    elif pferd_pos[0] < groesse - 1:
        pferd_pos[0] += 1

    # Schritt 4 – Ziel erreicht?
    if pferd_pos == ziel_pos:
        brett[pferd_pos[0]][pferd_pos[1]] = "🏆"
        spalten_buchstaben = "ABCDEF"
        koordinate = f"{spalten_buchstaben[pferd_pos[1]]}{pferd_pos[0] + 1}"
        print(f"Zug {zug}: Pferd auf Feld {koordinate}")
        print("🎉 ZIEL ERREICHT! Dressur abgeschlossen!")
        break
    else:
        brett[pferd_pos[0]][pferd_pos[1]] = "P"

    # Bonus – Koordinaten ausgeben
    spalten_buchstaben = "ABCDEF"
    koordinate = f"{spalten_buchstaben[pferd_pos[1]]}{pferd_pos[0] + 1}"
    print(f"Zug {zug}: Pferd auf Feld {koordinate}")

    if zug >= 15:
        break