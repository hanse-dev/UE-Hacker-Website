# Schritt 1: Helden anlegen
helden = [
    {"name": "Thorin", "klasse": "Krieger", "level": 10, "spezial": "Schildwall"},
    {"name": "Aria", "klasse": "Magierin", "level": 8, "spezial": "Feuerball"},
    {"name": "Drake", "klasse": "Krieger", "level": 6, "spezial": "Sturmhieb"},
    {"name": "Lyra", "klasse": "Bogenschützin", "level": 9, "spezial": "Zielsicher"}
]

# Schritt 2: Suche nach Klasse
print("=== HELDEN-ARCHIV ===")
for klasse in ["Krieger", "Magierin"]:
    gefunden = [h for h in helden if h["klasse"] == klasse]
    print(f"\nKlasse '{klasse}':")
    for h in gefunden:
        print(f"  {h['name']} (Level {h['level']})")

# Schritt 3: Rangliste
bester = max(helden, key=lambda h: h["level"])
print(f"\nBester Held: {bester['name']} (Level {bester['level']})")
print("\nRangliste (nach Level):")
rangliste = sorted(helden, key=lambda h: h["level"], reverse=True)
for i, h in enumerate(rangliste, 1):
    print(f"  {i}. {h['name']} | Level {h['level']} | {h['klasse']}")

# Bonus: letzte 3 Missionen als Tupel
helden[0]["missionen"] = ("Kobold-Lager", "Turm des Lichts", "Drachenhöhle")
print(f"\nBonus – Missionen von {helden[0]['name']}: {helden[0]['missionen']}")

print()
print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast den Archivar des Gildenarchivs besiegt!")
print("⭐ Titel erhalten: Meister der Steckbriefe")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 8 gemeistert!")
print("📚 Nächste Woche: JSON-Dateien und I/O!")