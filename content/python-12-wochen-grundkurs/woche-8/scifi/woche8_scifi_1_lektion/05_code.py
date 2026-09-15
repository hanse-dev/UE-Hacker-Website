# Beispiel 3: Dictionaries ändern und erweitern
schiff = {
    "name": "Nebula-Explorer",
    "typ": "Forschung",
    "crew": 150
}

print(f"Original: {schiff}")

# Wert ändern
schiff["crew"] = 200
print(f"Nach Crew-Änderung: {schiff}")

# Neues Element hinzufügen
schiff["kapitaen"] = "Captain Alex"
print(f"Nach Kapitän hinzufügen: {schiff}")

# Element entfernen
entfernt = schiff.pop("typ")
print(f"Entfernt: {entfernt}")
print(f"Nach entfernen: {schiff}")