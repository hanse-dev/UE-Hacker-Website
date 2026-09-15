erfolge = 0
print("=== HINDERNIS-SIMULATOR GESTARTET ===")
print()

# Level 1: Aufsitzen
pferd_groesse = 1.70  # Meter
reiter_gewicht = 65   # kg
if pferd_groesse >= 1.60 and reiter_gewicht <= 80:
    print("Level 1 ✅ – Aufsitzen gelingt! Pferd und Reiter passen zusammen.")
    erfolge += 1
else:
    print("Level 1 ❌ – Aufsitzen fehlgeschlagen!")

# Level 2: Gangwahl
gangart = "Schritt"
if gangart == "Schritt":
    print("Level 2 ✅ – Schritt gewählt. Ruhiger Start!")
    erfolge += 1
else:
    print("Level 2 ✅ – Trab gewählt. Gutes Tempo!")
    erfolge += 1

# Level 3: Geschwindigkeit
tempo = 72
if tempo >= 90:
    print("Level 3 ✅ – GALOPP! Volles Tempo!")
    erfolge += 1
elif tempo >= 70:
    print("Level 3 ✅ – Starker Trab! Sehr gut!")
    erfolge += 1
elif tempo >= 50:
    print("Level 3 ✅ – Leichter Trab. Gut!")
    erfolge += 1
elif tempo >= 30:
    print("Level 3 ❌ – Schritt. Zu langsam für Hindernisse!")
else:
    print("Level 3 ❌ – Stehengeblieben!")

# Level 4: Hindernisprüfung
hoehe = 80
breite = 60
schwierigkeit = 40
if hoehe <= 100:
    if breite <= 80:
        print("Level 4 ✅ – Hindernis gemeistert! Höhe und Breite im Limit.")
        erfolge += 1
    else:
        print("Level 4 ❌ – Hindernis zu breit!")
else:
    print("Level 4 ❌ – Hindernis zu hoch!")

# Level 5: Abmeldung
zeit = 58
fehler = 0
stil = 85
if zeit <= 60 or (fehler == 0 and stil >= 80):
    print("Level 5 ✅ – Perfekte Abmeldung! Fehlerfrei!")
    erfolge += 1
else:
    print("Level 5 ❌ – Abmeldung nicht bestanden!")

# Ergebnis
print()
print(f"=== ERGEBNIS: {erfolge}/5 Level bestanden ===")
if erfolge == 5:
    print("🏆 REITMEISTER! Perfekter Durchlauf!")
elif erfolge >= 3:
    print("⭐ Gut gemacht! Weiter so!")
else:
    print("💪 Weiter üben – du schaffst das!")