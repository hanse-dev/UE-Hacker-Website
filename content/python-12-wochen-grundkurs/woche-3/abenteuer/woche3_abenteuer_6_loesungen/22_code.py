# Schritt 1 – Quest-Phasen
phase1_ok = True
phase2_ok = True
phase3_ok = False
phase4_ok = True
phase5_ok = True

erfolgreiche_phasen = 0
if phase1_ok:
    erfolgreiche_phasen += 1
if phase2_ok:
    erfolgreiche_phasen += 1
if phase3_ok:
    erfolgreiche_phasen += 1
if phase4_ok:
    erfolgreiche_phasen += 1
if phase5_ok:
    erfolgreiche_phasen += 1

# Schritt 2 – Gefahrenstufe
gefahrenstufe = 2
if gefahrenstufe == 1:
    print("Gefahrenstufe 1: Kinderleicht")
elif gefahrenstufe == 2:
    print("Gefahrenstufe 2: Leicht")
elif gefahrenstufe == 3:
    print("Gefahrenstufe 3: Mittel")
elif gefahrenstufe == 4:
    print("Gefahrenstufe 4: Schwer")
else:
    print("Gefahrenstufe 5: EXTREM!")

# Schritt 3 – Zufallsereignisse
monster_angriff = False
falle_ausgeloest = True
schatz_gefunden = True

if monster_angriff:
    print("⚔️ Monsterangriff! -20 HP")
if falle_ausgeloest:
    print("🪤 Falle ausgelöst! -10 HP")
if schatz_gefunden:
    print("💰 Schatz gefunden! +200 XP")

# Schritt 4 – Erfolgsbedingung
print(f"Erfolgreiche Phasen: {erfolgreiche_phasen}/5")
if erfolgreiche_phasen >= 4 and gefahrenstufe <= 3:
    print("🏆 Quest erfolgreich abgeschlossen!")
else:
    print("Quest nicht vollständig bestanden.")

# Schritt 5 – Sonderaktionen
if gefahrenstufe >= 4 and erfolgreiche_phasen < 3:
    print("🚨 Rettung erforderlich!")

# Schritt 6 – Auswertung
gesamtpunkte = erfolgreiche_phasen * 100 - gefahrenstufe * 20
erfolgsquote = (erfolgreiche_phasen / 5) * 100
print(f"Gesamtpunkte: {gesamtpunkte}")
print(f"Erfolgsquote: {erfolgsquote:.0f}%")

print()
print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast die Sphinx der rätselhaften Wege besiegt!")
print("⭐ Titel erhalten: Meister der Entscheidungen")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 3 gemeistert!")
print("📚 Nächste Woche: Schleifen (for, while)!")