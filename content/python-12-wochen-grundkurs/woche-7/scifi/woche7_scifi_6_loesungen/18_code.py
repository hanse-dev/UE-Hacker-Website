import random

ziele = ["Ressourcen sammeln", "Feind aufklären", "Außenposten sichern", "Signal untersuchen"]
planeten = ["Kepler-9b", "Proxima-II", "Orion-5", "Nova-Prime"]
gefahrenstufen = [1, 2, 3, 4, 5]
crew_mitglieder = ["Commander Zara", "Pilot Rex", "Dr. Nova", "Engineer Kai"]

# Schritt 2 & 3: Missions-Briefing
print("=== MISSIONS-BRIEFING ===")
gesamt_gefahr = 0
for i in range(1, 4):
    ziel = random.choice(ziele)
    planet = random.choice(planeten)
    gefahr = random.choice(gefahrenstufen)
    leiter = random.choice(crew_mitglieder)  # Bonus
    gesamt_gefahr += gefahr
    print(f"\nMission {i}:")
    print(f"  Ziel:         {ziel}")
    print(f"  Planet:       {planet}")
    print(f"  Gefahrenstufe:{gefahr}/5")
    print(f"  Leiter:       {leiter}")

durchschnitt_gefahr = round(gesamt_gefahr / 3, 1)
print(f"\nDurchschnittliche Gefahrenstufe: {durchschnitt_gefahr}")