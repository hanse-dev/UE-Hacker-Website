import random
import math

pferde = ["Thunder", "Luna", "Blitz", "Silber", "Sturm", "Wolke"]

# Schritt 1: Startliste mischen
random.shuffle(pferde)
print("=== TURNIER-STARTLISTE ===")
for i, pferd in enumerate(pferde, 1):
    print(f"  Startnummer {i}: {pferd}")

# Schritt 2: Leistung auswürfeln
print("\nLeistungspunkte:")
punkte = {pferd: random.randint(1, 10) for pferd in pferde}
for pferd, p in sorted(punkte.items(), key=lambda x: x[1], reverse=True):
    print(f"  {pferd}: {p} Punkte")

# Schritt 3: 3 Runden Turnier
siege = {pferd: 0 for pferd in pferde}
print("\n=== TURNIER-RUNDEN ===")
for runde in range(1, 4):
    runden_punkte = {pferd: random.randint(1, 10) for pferd in pferde}
    sieger = max(runden_punkte, key=runden_punkte.get)
    siege[sieger] += 1
    print(f"Runde {runde}: {sieger} gewinnt!")

print("\n=== TURNIER-ERGEBNIS ===")
champion = max(siege, key=siege.get)
print(f"Turnierssieger: {champion} ({siege[champion]} Runden)")

# Bonus: Mindestpunkte für 60%
mindestpunkte = math.ceil(10 * 0.6)
print(f"\nBonus: Mindestpunkte für 60% Gewinnchance: {mindestpunkte}")