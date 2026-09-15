# Beispiel 2: Liste von Dictionaries
crew = [
    {
        "name": "Captain Alex",
        "rolle": "Kommandant",
        "alter": 35,
        "erfahrung": 15
    },
    {
        "name": "Dr. Zara",
        "rolle": "Wissenschaftlerin",
        "alter": 28,
        "erfahrung": 8
    },
    {
        "name": "Lt. Nova",
        "rolle": "Pilotin",
        "alter": 26,
        "erfahrung": 6
    }
]

print("=== Crew-Liste ===")
for mitglied in crew:
    print(f"{mitglied['name']} - {mitglied['rolle']} ({mitglied['alter']} Jahre)")

# Nach Erfahrung filtern
erfahrene = [m for m in crew if m['erfahrung'] > 10]
print(f"\nErfahrene Crew: {[m['name'] for m in erfahrene]}")