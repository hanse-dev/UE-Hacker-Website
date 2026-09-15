import random

# Schritt 1 – Variablen
energie = 100
distanz = 0
pausen = 0
besondere_ereignisse = []

print("=== MARATHON-REITEN STARTET ===")
print(f"Start-Energie: {energie}")
print()

# Schritt 1 – Haupt-Marathon-Schleife
while True:
    distanz += 1

    # Schritt 2 – Energieverbrauch
    verbrauch = random.randint(5, 15)
    energie -= verbrauch

    # Schritt 3 – Futter-Pause alle 8 Runden
    if distanz % 8 == 0:
        futter_bonus = random.randint(10, 25)
        energie += futter_bonus
        if energie > 100:
            energie = 100
        pausen += 1
        ereignis = f"Runde {distanz}: Futter-Pause! +{futter_bonus} Energie"
        besondere_ereignisse.append(ereignis)
        print(ereignis)

    # Schritt 3 – Energie aufgebraucht
    if energie <= 0:
        print(f"😴 Pferd erschöpft nach {distanz} Runden!")
        break

    # Statusmeldung alle 10 Runden
    if distanz % 10 == 0:
        print(f"Runde {distanz}: Energie={energie}")

    if distanz >= 100:
        print(f"🏆 Marathon-Champion! 100 Runden geschafft!")
        break

# Schritt 4 – Statistik
print()
print("=== MARATHON-AUSWERTUNG ===")
print(f"Gesamte Distanz: {distanz} Runden")
print(f"Futter-Pausen: {pausen}")
print(f"Letzte Energie: {energie}")
print(f"Besondere Ereignisse: {len(besondere_ereignisse)}")

print()
print("🎉 Abschluss-Challenge abgeschlossen!")
print("🏆 Du hast das Pferd der unendlichen Runden gemeistert!")
print("⭐ Titel erhalten: Meister des Rhythmus")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 4 gemeistert!")
print("🐴 Nächste Woche: Funktionen (def, return)!")