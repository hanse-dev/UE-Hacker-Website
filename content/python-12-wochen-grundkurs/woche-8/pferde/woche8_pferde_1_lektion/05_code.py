# Beispiel 3: Stallkarten ändern und erweitern
pferd = {
    "name": "Thunder",
    "rasse": "Hannoveraner",
    "alter": 8
}

print(f"Original: {pferd}")

# Wert ändern
pferd["alter"] = 9
print(f"Nach Geburtstag: {pferd}")

# Neues Element hinzufügen
pferd["besitzer"] = "Anna"
print(f"Nach Besitzer hinzufügen: {pferd}")

# Element entfernen
entfernt = pferd.pop("rasse")
print(f"Entfernt: {entfernt}")
print(f"Nach entfernen: {pferd}")