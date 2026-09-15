import random

# Schritt 1–4 – Sprung-Parcours mit 10 Sprüngen
gesamtpunkte = 0
hohe_spruenge = 0
hoechste_hoehe = 0
abwuerfe = []

print("=== SPRUNG-PARCOURS ===")
for sprung_nr in range(1, 11):
    # Schritt 1 – Zufällige Sprunghöhe
    hoehe = random.randint(60, 140)  # cm

    # Schritt 2 – Punkte vergeben
    if hoehe >= 130:
        punkte = 100
    elif hoehe >= 110:
        punkte = 80
    elif hoehe >= 90:
        punkte = 60
    else:
        punkte = 40

    # Bonus – Zufälliger Abwurf
    abwurf = random.choice([True, False, False, False])  # 25% Chance
    if abwurf:
        punkte -= 20
        abwuerfe.append(sprung_nr)

    gesamtpunkte += punkte

    # Schritt 2 – Zähle hohe Sprünge
    if hoehe > 100:
        hohe_spruenge += 1

    # Schritt 3 – Höchsten Sprung merken
    if hoehe > hoechste_hoehe:
        hoechste_hoehe = hoehe

    print(f"Sprung {sprung_nr:2d}: {hoehe}cm | Punkte: {punkte}{'  ❌ Abwurf!' if abwurf else ''}")

# Schritt 4 – Statistik
print()
print("=== SPRUNG-STATISTIK ===")
print(f"Gesamtpunkte: {gesamtpunkte}")
print(f"Sprünge über 100cm: {hohe_spruenge}/10")
print(f"Höchster Sprung: {hoechste_hoehe}cm")
print(f"Durchschnitt: {gesamtpunkte / 10:.0f} Punkte/Sprung")
if abwuerfe:
    print(f"Abwürfe bei Sprung: {abwuerfe}")