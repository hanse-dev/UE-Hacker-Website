typen = ["Halle", "Weide", "Stall"]
import random

stationen = [random.choice(typen) for i in range(5)]
alle_gueltig = True
for station in stationen:
    if station not in typen:
        alle_gueltig = False
print(f"Stationen: {len(stationen)}")
print(f"Alle gültig: {alle_gueltig}")
