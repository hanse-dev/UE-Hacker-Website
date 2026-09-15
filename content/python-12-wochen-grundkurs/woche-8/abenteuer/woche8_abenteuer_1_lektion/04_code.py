# Beispiel 2: Auf Steckbriefe zugreifen
held = {
    "name": "Aria",
    "klasse": "Magierin",
    "level": 15,
    "lebenspunkte": 120
}

print("=== Helden-Steckbrief auslesen ===")
print(f"Helden-Name: {held['name']}")
print(f"Klasse: {held['klasse']}")
print(f"Level: {held['level']}")
print(f"Lebenspunkte: {held['lebenspunkte']}")

# Mit get() Methode (sicherer)
print(f"\nMit get(): {held.get('name')}")
print(f"Nicht existierend: {held.get('mana', 'Unbekannt')}")