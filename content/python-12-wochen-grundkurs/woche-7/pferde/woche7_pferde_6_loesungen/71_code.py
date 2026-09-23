monster = ["Oxer", "Graben", "Mauer"]
import random

inhalte = []
monster_anzahl = 0
for raum in range(5):
    if random.randint(0, 1) == 1:
        inhalte.append(random.choice(monster))
    else:
        inhalte.append("leer")
for inhalt in inhalte:
    if inhalt != "leer":
        monster_anzahl += 1
print(f"Räume: {len(inhalte)}")
print(f"Anzahl passt: {0 <= monster_anzahl <= 5}")
