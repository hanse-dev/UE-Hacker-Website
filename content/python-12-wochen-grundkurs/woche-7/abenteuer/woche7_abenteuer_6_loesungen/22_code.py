import random

raum_typen = ["Schatzkammer", "Falle", "Leerer Raum", "Wachposten", "Altar"]
monster_liste = ["Goblin", "Skelett", "Troll", None, None]  # None = kein Monster

print("=== ZUFALLS-DUNGEON ===")
monster_count = 0

for i in range(1, 6):
    raum_typ = random.choice(raum_typen)
    monster = random.choice(monster_liste)
    if monster:
        monster_count += 1
        inhalt = f"Monster: {monster}"
    else:
        inhalt = "Sicher – kein Monster"
    print(f"Raum {i}: {raum_typ} | {inhalt}")

benoetigte_leben = (monster_count + 1) // 2
print(f"\nMonster gesamt: {monster_count}")
print(f"Benötigte Leben: {benoetigte_leben}")

print()
print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast den Archivar der geliehenen Zauber besiegt!")
print("⭐ Titel erhalten: Meister der Bibliothek von Pyralia")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 7 gemeistert!")
print("📚 Nächste Woche: Dictionaries und Tupel!")
