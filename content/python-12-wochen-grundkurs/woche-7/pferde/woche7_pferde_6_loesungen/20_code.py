import random
import math

pferde_namen = ["Thunder", "Luna", "Blitz", "Silber"]

# Schritt 1: Gewichte bestimmen
print("=== FUTTERKALKULATOR ===")
print("Gewichte der Pferde:")
pferde_daten = []
for name in pferde_namen:
    gewicht = random.randint(300, 600)
    pferde_daten.append((name, gewicht))
    print(f"  {name}: {gewicht} kg")

# Schritt 2: Tagesrationen berechnen (2% Körpergewicht)
print("\nTagesrationen (2% Körpergewicht):")
gesamt_tag = 0
rationen = []
for name, gewicht in pferde_daten:
    ration = math.ceil(gewicht * 0.02)
    rationen.append((name, ration))
    gesamt_tag += ration
    print(f"  {name}: {ration} kg/Tag")

# Schritt 3: Wochenplan
gesamt_woche = gesamt_tag * 7
print(f"\nGesamtfutter pro Tag:  {gesamt_tag} kg")
print(f"Gesamtfutter pro Woche: {gesamt_woche} kg")

# Bonus: Säcke (25 kg je Sack)
saecke = math.ceil(gesamt_woche / 25)
print(f"\nBonus: Benötigte Futtersäcke (25 kg): {saecke} Säcke")