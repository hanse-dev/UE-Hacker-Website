# Beispiel 3: Tupel unpacking und Methoden
schiff_daten = ("Nebula-Explorer", "Forschung", 150, 0.8)

# Tupel unpacking
name, typ, crew, geschwindigkeit = schiff_daten
print("=== Tupel Unpacking ===")
print(f"Name: {name}")
print(f"Typ: {typ}")
print(f"Crew: {crew}")
print(f"Geschwindigkeit: {geschwindigkeit}")

# Tupel-Methoden
print(f"\nAnzahl Elemente: {len(schiff_daten)}")
print(f"Index von 'Forschung': {schiff_daten.index('Forschung')}")
print(f"Anzahl 'Forschung': {schiff_daten.count('Forschung')}")