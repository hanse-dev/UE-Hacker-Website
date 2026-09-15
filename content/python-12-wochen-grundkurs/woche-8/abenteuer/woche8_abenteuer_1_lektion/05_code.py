# Beispiel 3: Steckbriefe ändern und erweitern
held = {
    "name": "Aria",
    "klasse": "Magierin",
    "level": 15
}

print(f"Original: {held}")

# Wert ändern
held["level"] = 16
print(f"Nach Level-Up: {held}")

# Neue Eigenschaft hinzufügen
held["mana"] = 80
print(f"Nach Mana hinzufügen: {held}")

# Eintrag entfernen
entfernt = held.pop("klasse")
print(f"Entfernt: {entfernt}")
print(f"Nach entfernen: {held}")