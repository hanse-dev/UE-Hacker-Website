erfolge = 0
print("=== DUNGEON-SIMULATOR GESTARTET ===")
print()

# Level 1: Beschwörung
mana = 75
zauber_bereit = True
if mana >= 50 and zauber_bereit:
    print("Level 1 ✅ – Beschwörung gelingt! Mana ausreichend und Zauber bereit.")
    erfolge += 1
else:
    print("Level 1 ❌ – Beschwörung fehlgeschlagen!")

# Level 2: Wegwahl
weg = "Links"
if weg == "Links":
    print("Level 2 ✅ – Du gehst nach Links. Dort liegt der Schatz!")
    erfolge += 1
else:
    print("Level 2 ❌ – Rechts war die Falle. Zurück!")

# Level 3: Geschwindigkeit
tempo = 65
if tempo >= 90:
    print("Level 3 ✅ – BLITZ-Tempo! Unaufhaltbar!")
    erfolge += 1
elif tempo >= 70:
    print("Level 3 ✅ – Schnell! Du entwischst dem Monster!")
    erfolge += 1
elif tempo >= 50:
    print("Level 3 ✅ – Gutes Tempo, du kommst durch.")
    erfolge += 1
elif tempo >= 30:
    print("Level 3 ❌ – Zu langsam, das Monster erwischt dich!")
else:
    print("Level 3 ❌ – Viel zu langsam!")

# Level 4: Magieprüfung
schutz = 80
angriff = 70
heilung = 60
if schutz >= 70:
    if angriff >= 60:
        print("Level 4 ✅ – Schutz und Angriff stark genug!")
        erfolge += 1
    else:
        print("Level 4 ❌ – Angriff zu schwach!")
else:
    print("Level 4 ❌ – Schutz zu gering!")

# Level 5: Flucht
traenke = 4
runen = True
fluchtweg = True
if traenke >= 3 or (runen and fluchtweg):
    print("Level 5 ✅ – Flucht gelingt! Entkommen!")
    erfolge += 1
else:
    print("Level 5 ❌ – Kein Entkommen!")

# Ergebnis
print()
print(f"=== ERGEBNIS: {erfolge}/5 Level bestanden ===")
if erfolge == 5:
    print("🏆 DUNGEON-MEISTER! Perfekter Durchlauf!")
elif erfolge >= 3:
    print("⭐ Gut gemacht! Aber da ist noch Luft nach oben.")
else:
    print("💪 Weiter üben – du schaffst das!")