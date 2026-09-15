# Schritt 1: Liste von Dictionaries
crew = [
    {"name": "Captain Zara", "rang": "Kommandantin", "alter": 38, "erfahrung": 15},
    {"name": "Dr. Orion", "rang": "Arzt", "alter": 42, "erfahrung": 18},
    {"name": "Tech Maya", "rang": "Ingenieurin", "alter": 29, "erfahrung": 6},
]

print("=== Crew-Datenbank ===")
for m in crew:
    print(f"  {m['name']} | {m['rang']} | {m['erfahrung']} Jahre")

# Schritt 2: Suche
veteran = next(m for m in crew if m["erfahrung"] == max(c["erfahrung"] for c in crew))
print(f"\nErfahrenste: {veteran['name']} ({veteran['erfahrung']} Jahre)")

# Schritt 3: Sortieren
crew.sort(key=lambda m: m["alter"])
print("\nNach Alter:")
for m in crew:
    print(f"  {m['name']}: {m['alter']} Jahre")