erfolge = 0
print("=== RAUMSCHIFF-SIMULATOR GESTARTET ===")
print()

# Level 1: Startsequenz
energie = 80
system_ok = True
if energie >= 50 and system_ok:
    print("Level 1 ✅ – Startsequenz erfolgreich! Alle Systeme online.")
    erfolge += 1
else:
    print("Level 1 ❌ – Startsequenz fehlgeschlagen!")

# Level 2: Kurswahl
kurs = "Nord"
if kurs == "Nord":
    print("Level 2 ✅ – Kurs Nord eingeschlagen. Richtung Andromeda!")
    erfolge += 1
else:
    print("Level 2 ✅ – Kurs Süd eingeschlagen. Richtung Centaurus!")
    erfolge += 1

# Level 3: Geschwindigkeit
geschwindigkeit = 650
if geschwindigkeit >= 900:
    print("Level 3 ✅ – WARP! Lichtgeschwindigkeit erreicht!")
    erfolge += 1
elif geschwindigkeit >= 700:
    print("Level 3 ✅ – Sehr schnell! Sub-Warp-Antrieb aktiv.")
    erfolge += 1
elif geschwindigkeit >= 500:
    print("Level 3 ✅ – Gute Reisegeschwindigkeit.")
    erfolge += 1
elif geschwindigkeit >= 200:
    print("Level 3 ❌ – Zu langsam für diese Mission!")
else:
    print("Level 3 ❌ – Antrieb fast ohne Schub!")

# Level 4: Systemprüfung
schilde = 85
waffen = 70
antrieb = 90
if schilde >= 70:
    if waffen >= 60:
        print("Level 4 ✅ – Schilde und Waffen einsatzbereit!")
        erfolge += 1
    else:
        print("Level 4 ❌ – Waffensysteme zu schwach!")
else:
    print("Level 4 ❌ – Schilde zu gering – Gefahr!")

# Level 5: Notlandung
treibstoff = 25
atmosphaere = True
landeplatz = True
if treibstoff >= 20 or (atmosphaere and landeplatz):
    print("Level 5 ✅ – Notlandung erfolgreich! Sicher gelandet.")
    erfolge += 1
else:
    print("Level 5 ❌ – Notlandung fehlgeschlagen!")

# Ergebnis
print()
print(f"=== ERGEBNIS: {erfolge}/5 Level bestanden ===")
if erfolge == 5:
    print("🏆 PILOTEN-LIZENZ ERWORBEN! Perfekter Simulator-Lauf!")
elif erfolge >= 3:
    print("⭐ Gut! Noch etwas Übung nötig.")
else:
    print("💪 Weitersimulieren – du wirst besser!")