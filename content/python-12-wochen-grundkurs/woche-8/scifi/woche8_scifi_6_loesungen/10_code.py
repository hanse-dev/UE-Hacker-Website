# Schritt 1: Schiff-Dictionary
schiff = {
    "name": "Nebula-7",
    "typ": "Forschungsschiff",
    "crew": 150,
    "geschwindigkeit": 9.5
}
print(schiff)

# Schritt 2: Werte ändern
schiff["crew"] = 165
schiff["status"] = "aktiv"
print(f"Crew: {schiff['crew']}")
print(f"Status: {schiff['status']}")

# Schritt 3: Ausgabe
print("\n=== Schiffsdaten ===")
for schluessel, wert in schiff.items():
    print(f"  {schluessel}: {wert}")