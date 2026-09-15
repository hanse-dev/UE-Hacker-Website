# Schritt 1–3 – Primzahlen (magische Zahlen) von 2 bis 100 finden
magische_zahlen = []

for zahl in range(2, 101):
    ist_prim = True
    # Schritt 2 – Primzahl-Test mit verschachtelter Schleife
    for teiler in range(2, zahl):
        if zahl % teiler == 0:
            ist_prim = False
            break
    if ist_prim:
        magische_zahlen.append(zahl)
        print(f"★ Magische Zahl gefunden: {zahl}")

# Schritt 4 – Visualisierung
print()
print(f"Insgesamt {len(magische_zahlen)} magische Zahlen zwischen 2 und 100:")
visualisierung = ""
for z in magische_zahlen:
    visualisierung += f"★{z} "
print(visualisierung)
print(f"Größte magische Zahl: {magische_zahlen[-1]}")
print(f"Summe aller magischen Zahlen: {sum(magische_zahlen)}")