# Schritt 1: Helden-Steckbrief anlegen
held = {
    "name": "Thorin",
    "klasse": "Krieger",
    "level": 5,
    "lebenspunkte": 120
}
print("Helden-Steckbrief:")
print(held)

# Schritt 2: Werte ändern und ergänzen
held["level"] = 6
held["mana"] = 80
print(f"\nNach Update: Level {held['level']}, Mana {held['mana']}")

# Schritt 3: Monster-Liste aus Dictionaries
monster = [
    {"name": "Goblin", "typ": "Schwach", "staerke": 10},
    {"name": "Troll", "typ": "Stark", "staerke": 45},
    {"name": "Drache", "typ": "Boss", "staerke": 100}
]
print(f"\nMonster-Liste: {monster}")
print(f"Erstes Monster: {monster[0]['name']}")

# Schritt 4: Zugriff und Ausgabe
name = held["name"]
klasse = held.get("klasse")
print(f"\n=== HELD: {name}, Klasse: {klasse}, Level: {held['level']} ===")

# Bonus: Verschachteltes Dictionary
held["ausruestung"] = {"waffe": "Kriegshammer", "ruestung": "Kettenhemd"}
print(f"Waffe: {held['ausruestung']['waffe']}")