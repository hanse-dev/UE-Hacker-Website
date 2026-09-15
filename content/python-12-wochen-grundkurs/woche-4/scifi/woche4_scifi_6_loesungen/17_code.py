# Primzahlen von 2 bis 100
primzahlen = []
for zahl in range(2, 101):
    ist_prim = True
    for teiler in range(2, zahl):
        if zahl % teiler == 0:
            ist_prim = False
            break
    if ist_prim:
        primzahlen.append(zahl)

print(f"Primzahlen bis 100: {primzahlen}")
print(f"Anzahl: {len(primzahlen)}")
print(f"Größte Primzahl: {primzahlen[-1]}")
print(f"Summe: {sum(primzahlen)}")