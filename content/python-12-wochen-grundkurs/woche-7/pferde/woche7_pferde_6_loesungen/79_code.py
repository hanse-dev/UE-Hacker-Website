import random

position = 0
karte = [0]
schritte = 0
while schritte < 100:
    position += random.choice([-1, 1])
    karte.append(position)
    schritte += 1
    if position == 5:
        break
print(f"Höchstens 100 Schritte: {schritte <= 100}")
print(f"Karte passt: {len(karte) == schritte + 1}")
