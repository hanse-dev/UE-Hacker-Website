# Schritt 1: Schatz-Steckbrief
schatz1 = {"name": "Rubinring", "wert": 800, "ort": "Drachenhöhle", "seltenheit": "Legendär"}
print("=== SCHATZARCHIV ===")
for schluessel, wert in schatz1.items():
    print(f"  {schluessel}: {wert}")

# Schritt 2: 3 Schätze sammeln
schaetze = [
    {"name": "Rubinring", "wert": 800, "ort": "Drachenhöhle", "seltenheit": "Legendär"},
    {"name": "Silberschwert", "wert": 350, "ort": "Turm des Lichts", "seltenheit": "Selten"},
    {"name": "Goldkrone", "wert": 1200, "ort": "Elfenwald", "seltenheit": "Einmalig"}
]

# Schritt 3: Archiv durchsuchen
print("\nWertvolle Schätze (> 500 Gold):")
gesamtwert = 0
for s in schaetze:
    gesamtwert += s["wert"]
    if s["wert"] > 500:
        print(f"  {s['name']}: {s['wert']} Gold ({s['seltenheit']})")
print(f"Gesamtwert aller Schätze: {gesamtwert} Gold")

# Bonus: Sortierung nach Wert
sortiert = sorted(schaetze, key=lambda s: s["wert"], reverse=True)
print("\nSortiert nach Wert (höchster zuerst):")
for s in sortiert:
    print(f"  {s['name']}: {s['wert']} Gold")