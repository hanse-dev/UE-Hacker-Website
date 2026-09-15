# Schritt 1 – Missionsphasen
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

# Schritt 2 – Gefahrenstufe
gefahrenstufe = 2
if gefahrenstufe == 1:
    print("Gefahrenstufe 1: Grüner Sektor")
elif gefahrenstufe == 2:
    print("Gefahrenstufe 2: Gelber Sektor")
elif gefahrenstufe == 3:
    print("Gefahrenstufe 3: Oranger Sektor")
elif gefahrenstufe == 4:
    print("Gefahrenstufe 4: Roter Sektor")
else:
    print("Gefahrenstufe 5: SCHWARZES LOCH!")

# Schritt 3 – Zufallsereignisse
meteor_treffer = False
piraten_angriff = True
system_ausfall = False

if meteor_treffer:
    print("☄️ Meteortreffer! -30 Schilde")
if piraten_angriff:
    print("🏴‍☠️ Piratenangriff! Abwehrsysteme aktiviert!")
if system_ausfall:
    print("💻 Systemausfall! Notprogramm läuft...")

# Schritt 4 – Erfolgsbedingung
print(f"Erfolgreiche Phasen: {erfolgreiche_phasen}/5")
if erfolgreiche_phasen >= 4 and gefahrenstufe <= 3:
    print("🏆 Mission erfolgreich! Galaxie gerettet!")
else:
    print("Mission nicht vollständig bestanden.")

# Schritt 5 – Sonderaktionen
if gefahrenstufe >= 4 and erfolgreiche_phasen < 3:
    print("🚨 Rettungsaktion erforderlich!")

# Schritt 6 – Missionsauswertung
gesamtpunkte = erfolgreiche_phasen * 100 - gefahrenstufe * 20
erfolgsquote = (erfolgreiche_phasen / 5) * 100
print(f"Gesamtpunkte: {gesamtpunkte}")
print(f"Erfolgsquote: {erfolgsquote:.0f}%")

print()
print("🎉 Finale Herausforderung abgeschlossen!")
print("🏆 Du hast den KI-Hüter der paradoxen Entscheidungen besiegt!")
print("⭐ Titel erhalten: Meister der Pfade")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 3 gemeistert!")
print("🚀 Nächste Woche: Schleifen (for, while)!")