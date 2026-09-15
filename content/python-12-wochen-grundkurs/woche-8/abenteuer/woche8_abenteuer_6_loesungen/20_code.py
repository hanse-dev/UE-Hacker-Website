# Schritt 1: Dungeon aufbauen
dungeon = {
    "Ebene 1": {"monster": "Goblin", "schatz": "Kupfermünzen", "schwierigkeit": 2},
    "Ebene 2": {"monster": "Troll", "schatz": "Silberdolch", "schwierigkeit": 5},
    "Ebene 3": {"monster": "Drache", "schatz": "Rubinkrone", "schwierigkeit": 9}
}

# Schritt 2: Ebenen erkunden
print("=== DUNGEON-MANAGER ===")
gefaehrlichste = max(dungeon, key=lambda e: dungeon[e]["schwierigkeit"])
for ebene, daten in dungeon.items():
    print(f"\n{ebene}:")
    print(f"  Monster:        {daten['monster']}")
    print(f"  Schatz:         {daten['schatz']}")
    print(f"  Schwierigkeit:  {daten['schwierigkeit']}/10")
print(f"\nGefährlichste Ebene: {gefaehrlichste}")

# Schritt 3: Held schicken
held = {"name": "Thorin", "klasse": "Krieger", "level": 5}
print(f"\nHeld: {held['name']} (Level {held['level']})")
print("Zugängliche Ebenen:")
for ebene, daten in dungeon.items():
    if held["level"] >= daten["schwierigkeit"]:
        print(f"  ✓ {ebene} (Schwierigkeit {daten['schwierigkeit']})")
    else:
        print(f"  ✗ {ebene} (Schwierigkeit {daten['schwierigkeit']}) – zu gefährlich!")

# Bonus: Level-Up nach Ebene
print("\nBonus – Level-Up nach Erkundung:")
for ebene in dungeon:
    if held["level"] >= dungeon[ebene]["schwierigkeit"]:
        held["level"] += 1
        print(f"  {ebene} besiegt! Neues Level: {held['level']}")