import random

wuerfe = []
for spieler in range(3):
    wuerfe.append(random.randint(1, 6))
alle_ok = True
for wurf in wuerfe:
    if wurf < 1 or wurf > 6:
        alle_ok = False
print(f"Spieler: {len(wuerfe)}")
print(f"Alle im Bereich: {alle_ok}")
