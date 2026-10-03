gefahren = ["Drohne", "Alien", "Roboter"]
import random

inhalte = []
gefahren_anzahl = 0
for raum in range(5):
    if random.randint(0, 1) == 1:
        inhalte.append(random.choice(gefahren))
    else:
        inhalte.append("leer")
for inhalt in inhalte:
    if inhalt != "leer":
        gefahren_anzahl += 1
print(f"Räume: {len(inhalte)}")
print(f"Anzahl passt: {0 <= gefahren_anzahl <= 5}")
