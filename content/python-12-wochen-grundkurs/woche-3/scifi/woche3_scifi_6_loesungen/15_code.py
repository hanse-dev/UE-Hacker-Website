# Schritt 1 – Missionsdaten
missions_level = 10
erfolgspunkte = 95
verluste = 0
zeit = 25  # Sekunden

# Schritt 2 – Gesamtnote
note = erfolgspunkte - (verluste * 10) - (zeit / 5)
print(f"Level: {missions_level}, Punkte: {erfolgspunkte}, Verluste: {verluste}, Zeit: {zeit}s")
print(f"Gesamtnote: {note:.1f}")

# Schritt 3 – Legendär-Status
if missions_level >= 10 and note >= 85 and verluste == 0:
    print("🏆 LEGENDÄR! Absolutist Perfektion – Galaktische Ehre!")
elif missions_level >= 8 and note >= 70 and verluste <= 2:
    print("⭐ EXZELLENT! Hervorragende Leistung!")
elif missions_level >= 5:
    print("👍 GUT – Mission erfüllt!")
else:
    print("Mission mit Schwierigkeiten abgeschlossen.")

# Schritt 5 – Blitz-Bonus
if zeit < 30:
    print("+50 Bonus für Blitzmission!")