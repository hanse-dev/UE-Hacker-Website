hindernisse = ["Oxer", "Graben", "Mauer"]
import random

inhalte = []
hindernis_anzahl = 0
for station in range(5):
    if random.randint(0, 1) == 1:
        inhalte.append(random.choice(hindernisse))
    else:
        inhalte.append("leer")
for inhalt in inhalte:
    if inhalt != "leer":
        hindernis_anzahl += 1
print(f"Stationen: {len(inhalte)}")
print(f"Anzahl passt: {0 <= hindernis_anzahl <= 5}")
