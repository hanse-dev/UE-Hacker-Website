primzahlen = []
for n in range(2, 101):
    ist_prim = True
    for i in range(2, n):
        if n % i == 0:
            ist_prim = False
    if ist_prim:
        primzahlen.append(n)
print(f"Anzahl: {len(primzahlen)}")
print(f"Größte: {primzahlen[-1]}")
