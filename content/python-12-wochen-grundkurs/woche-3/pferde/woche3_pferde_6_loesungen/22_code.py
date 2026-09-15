# Schritt 1 – Turnierphasen
phase1_ok = True
phase2_ok = True
phase3_ok = True
phase4_ok = False
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

# Schritt 2 – Schwierigkeitsstufe
schwierigkeit = 3
if schwierigkeit == 1:
    print("Schwierigkeit 1: Anfänger")
elif schwierigkeit == 2:
    print("Schwierigkeit 2: Fortgeschritten")
elif schwierigkeit == 3:
    print("Schwierigkeit 3: Turnier")
elif schwierigkeit == 4:
    print("Schwierigkeit 4: Championat")
else:
    print("Schwierigkeit 5: OLYMPIA!")

# Schritt 3 – Zufallsereignisse
hindernis_umgeworfen = False
pferd_scheut = False
sattel_verrutscht = True

if hindernis_umgeworfen:
    print("❌ Hindernis umgeworfen! -5 Punkte")
if pferd_scheut:
    print("😨 Pferd scheut! -10 Punkte")
if sattel_verrutscht:
    print("⚠️ Sattel verrutscht! -3 Punkte")

# Schritt 4 – Erfolgsbedingung
print(f"Erfolgreiche Phasen: {erfolgreiche_phasen}/5")
if erfolgreiche_phasen >= 4 and schwierigkeit <= 3:
    print("🏆 Turniersieg! Großartige Leistung!")
else:
    print("Turnier nicht gewonnen – nächstes Mal!")

# Schritt 5 – Sonderaktionen
if schwierigkeit >= 4 and erfolgreiche_phasen < 3:
    print("📋 Zusatztraining erforderlich!")

# Schritt 6 – Auswertung
gesamtpunkte = erfolgreiche_phasen * 100 - schwierigkeit * 20
platzierung = (erfolgreiche_phasen / 5) * 100
print(f"Gesamtpunkte: {gesamtpunkte}")
print(f"Platzierung: {platzierung:.0f}%")

print()
print("🎉 Abschluss-Challenge abgeschlossen!")
print("🏆 Du hast das Pferd der unentschlossenen Wege gemeistert!")
print("⭐ Titel erhalten: Meister der Weichen")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 3 gemeistert!")
print("🐴 Nächste Woche: Schleifen (for, while)!")