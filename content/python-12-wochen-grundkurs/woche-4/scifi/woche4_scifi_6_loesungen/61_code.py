for zahl in range(2, 31):
    ist_primzahl = True
    for a in range(2, zahl):
        for b in range(2, zahl):
            if a * b == zahl:
                ist_primzahl = False
    if ist_primzahl:
        print("P", end="")
    else:
        print(".", end="")
print()
