# Beispiel 2: Liste von Steckbriefen
helden = [
    {
        "name": "Aria",
        "klasse": "Magierin",
        "level": 15,
        "erfahrung": 2500
    },
    {
        "name": "Thorin",
        "klasse": "Krieger",
        "level": 18,
        "erfahrung": 3200
    },
    {
        "name": "Luna",
        "klasse": "Schurkin",
        "level": 12,
        "erfahrung": 1800
    }
]

print("=== Helden-Liste ===")
for held in helden:
    print(f"{held['name']} - {held['klasse']} (Level {held['level']})")

# Nach Level filtern
starke = [h for h in helden if h['level'] > 14]
print(f"\nStarke Helden: {[h['name'] for h in starke]}")