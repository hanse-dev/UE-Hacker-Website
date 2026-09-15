# Beispiel 3: Nützliche Listen-Operationen
monster = ["Goblin", "Ork", "Troll", "Drache", "Goblin", "Ork"]

print("=== Listen-Operationen ===")
print(f"Monster-Liste: {monster}")
print(f"Anzahl Monster: {len(monster)}")

# Einzigartige Elemente: set() entfernt Duplikate
# set ist eine Sammlung ohne Reihenfolge und ohne Duplikate
einzigartige_monster = list(set(monster))
print(f"Einzigartige Monster: {einzigartige_monster}")

# Mit enumerate() Index und Wert gleichzeitig
print("\nAlle Monster mit Position:")
for index, m in enumerate(monster):
    print(f"  Position {index}: {m}")
