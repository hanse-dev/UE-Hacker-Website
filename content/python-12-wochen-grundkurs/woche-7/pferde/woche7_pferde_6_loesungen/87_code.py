feld = []
for zeile in range(8):
    reihe = []
    for spalte in range(8):
        reihe.append(0)
    feld.append(reihe)
figur = [0, 0]
ziel = [7, 7]
zuege = 0
while True:
    if figur == ziel:
        break
    if figur[1] < 7:
        figur[1] += 1
    else:
        figur[0] += 1
    zuege += 1
print(f"Züge: {zuege}")
print(f"Ziel erreicht: {figur == ziel}")
