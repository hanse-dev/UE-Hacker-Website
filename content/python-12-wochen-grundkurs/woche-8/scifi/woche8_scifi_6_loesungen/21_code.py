# Liste von Missions-Dictionaries
missionen = [
    {"name": "Alpha", "planet": "Kepler-62", "ergebnis": "erfolgreich", "dauer": 30},
    {"name": "Beta", "planet": "Gliese-667", "ergebnis": "abgebrochen", "dauer": 7},
    {"name": "Gamma", "planet": "Proxima", "ergebnis": "erfolgreich", "dauer": 45},
    {"name": "Delta", "planet": "HD 40307", "ergebnis": "erfolgreich", "dauer": 22},
]

# Suche: erfolgreiche Missionen
erfolgreich = [m for m in missionen if m["ergebnis"] == "erfolgreich"]
print(f"Erfolgreiche Missionen: {len(erfolgreich)} von {len(missionen)}")

# Gesamtdauer
gesamt = sum(m["dauer"] for m in missionen)
print(f"Gesamtdauer: {gesamt} Tage")

# Kürzeste erfolgreiche Mission
kuerzeste = min(erfolgreich, key=lambda m: m["dauer"])
print(f"Kürzeste Erfolgs-Mission: {kuerzeste['name']} ({kuerzeste['dauer']} Tage)")

print()
print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast den Daten-Kurator der unendlichen Schlüssel besiegt!")
print("⭐ Titel erhalten: Meister der Daten-Archive")