import random

spieler = ["Merlin", "Aria", "Dragan"]
siege = {name: 0 for name in spieler}

print("=== WÜRFELTURNIER ===")

for runde in range(1, 6):
    print(f"\nRunde {runde}:")
    wuerfe = {}
    for name in spieler:
        wurf = random.randint(1, 6)
        wuerfe[name] = wurf
        print(f"  {name} würfelt: {wurf}")

    bester = max(wuerfe, key=wuerfe.get)
    siege[bester] += 1
    print(f"  -> Gewinner: {bester}!")

print("\n=== TURNIER-ERGEBNIS ===")
for name, anzahl in siege.items():
    print(f"  {name}: {anzahl} Runden gewonnen")
champion = max(siege, key=siege.get)
print(f"\nGesamtsieger: {champion}!")

# Bonus: Magiewürfel
print("\n=== BONUS: Magiewürfel-Runde (1-20) ===")
for name in spieler:
    magie_wurf = random.randint(1, 20)
    print(f"  {name}: {magie_wurf}")
