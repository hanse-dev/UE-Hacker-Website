# Schritt 1: Register anlegen
register = [
    {"pferd": "Thunder", "reiter": "Lena", "disziplin": "Dressur"},
    {"pferd": "Luna", "reiter": "Tom", "disziplin": "Gelaenderitt"},
    {"pferd": "Blitz", "reiter": "Sophie", "disziplin": "Springen"},
    {"pferd": "Silber", "reiter": "Max", "disziplin": "Dressur"}
]

# Schritt 2: Suche nach Disziplin
print("=== REITERHOF-REGISTER ===")
for disziplin in ["Dressur", "Springen"]:
    treffer = [e for e in register if e["disziplin"] == disziplin]
    print(f"\nDisziplin '{disziplin}':")
    for e in treffer:
        print(f"  {e['reiter']} auf {e['pferd']}")

# Schritt 3: Statistik
disziplin_zaehler = {}
for e in register:
    d = e["disziplin"]
    disziplin_zaehler[d] = disziplin_zaehler.get(d, 0) + 1

print(f"\nAnzahl verschiedener Disziplinen: {len(disziplin_zaehler)}")
beliebteste = max(disziplin_zaehler, key=disziplin_zaehler.get)
print(f"Beliebteste Disziplin: {beliebteste} ({disziplin_zaehler[beliebteste]}x)")

# Bonus: letzte 3 Trainingsdaten
register[0]["trainings"] = ("2026-06-01", "2026-06-08", "2026-06-15")
print(f"\nBonus – Letzte Trainings von {register[0]['reiter']}: {register[0]['trainings']}")

print()
print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast den Stallmeister der unendlichen Archive besiegt!")
print("⭐ Titel erhalten: Meister der Stall-Archive")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 8 gemeistert!")
print("📚 Nächste Woche: JSON-Dateien und I/O!")