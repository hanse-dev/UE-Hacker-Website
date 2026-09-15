# Schritt 1: Schiffsliste
schiffe = ["Nebula-Explorer", "Star-Fighter", "Nova-Hawk", "Iron-Wing", "Void-Runner"]
print(schiffe)

# Schritt 2: Elemente ergänzen
schiffe.append("Shadow-Cruiser")
schiffe.insert(1, "Alpha-Scout")
print(schiffe)

# Schritt 3: Element entfernen
schiffe.remove("Iron-Wing")
print(schiffe)

# Schritt 4: Sortieren & suchen
schiffe.sort()
print(f"Sortiert: {schiffe}")
print(f"Anzahl: {len(schiffe)}")
if "Nova-Hawk" in schiffe:
    print(f"Nova-Hawk an Index: {schiffe.index('Nova-Hawk')}")