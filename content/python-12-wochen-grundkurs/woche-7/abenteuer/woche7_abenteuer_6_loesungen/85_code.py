brett = []
for zeile in range(8):
    reihe = []
    for spalte in range(8):
        if (zeile + spalte) % 2 == 0:
            reihe.append("#")
        else:
            reihe.append(".")
    brett.append(reihe)
for zeile in range(2):
    print(" ".join(brett[zeile]))
