# Beispiel 2: Auf Dictionary-Elemente zugreifen
schiff = {
    "name": "Nebula-Explorer",
    "typ": "Forschung",
    "crew": 150,
    "geschwindigkeit": 0.8
}

print("=== Schiff-Zugriff ===")
print(f"Schiff-Name: {schiff['name']}")
print(f"Schiff-Typ: {schiff['typ']}")
print(f"Crew-Größe: {schiff['crew']}")
print(f"Geschwindigkeit: {schiff['geschwindigkeit']}c")

# Mit get() Methode (sicherer)
print(f"\nMit get(): {schiff.get('name')}")
print(f"Nicht existierend: {schiff.get('raumschiff', 'Unbekannt')}")