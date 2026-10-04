zahl = 15
ist_primzahl = True
for a in range(2, zahl):
    for b in range(2, zahl):
        if a * b == zahl:
            ist_primzahl = False
print(f"{zahl} ist Primzahl: {ist_primzahl}")
