typen = ["Frachtraum", "Reaktor", "Leerer Raum"]
import random

raeume = [random.choice(typen) for i in range(5)]
alle_gueltig = True
for raum in raeume:
    if raum not in typen:
        alle_gueltig = False
print(f"Räume: {len(raeume)}")
print(f"Alle gültig: {alle_gueltig}")
