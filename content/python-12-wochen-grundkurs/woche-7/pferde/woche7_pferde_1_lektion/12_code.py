# Beispiel 2: Aus Listen wählen
import random

print("=== Zufallsauswahl aus Listen ===")

# Pferde auf dem Hof
pferde = ["Thunder", "Stormy", "Sunny", "Shadow", "Blaze", "Misty"]
print(f"Alle Pferde: {pferde}")

# Ein zufälliges Pferd
ziel = random.choice(pferde)
print(f"Zielpferd: {ziel}")

# Drei zufällige Pferde
gruppe = random.choices(pferde, k=3)
print(f"Reitgruppe: {gruppe}")

# Liste mischen
reihenfolge = pferde.copy()
random.shuffle(reihenfolge)
print(f"Gemischte Reihenfolge: {reihenfolge}")