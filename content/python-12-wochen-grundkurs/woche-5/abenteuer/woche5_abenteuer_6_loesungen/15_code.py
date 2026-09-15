import random

# Schritt 1 – Quest-Daten erzeugen
def erstelle_quest(name, typ, schwierigkeit):
    return {"name": name, "typ": typ, "schwierigkeit": schwierigkeit}

# Schritt 2 – Belohnung berechnen
def berechne_belohnung(schwierigkeit, typ):
    typ_bonus = {"Kampf": 50, "Erkundung": 30, "Lieferung": 20}
    xp = schwierigkeit * 100 + typ_bonus.get(typ, 0)
    gold = schwierigkeit * 20 + typ_bonus.get(typ, 0) // 2
    return {"xp": xp, "gold": gold}

# Schritt 3 – Voraussetzungen prüfen
def pruefe_voraussetzung(held_level, schwierigkeit):
    mindest_level = schwierigkeit * 2
    return held_level >= mindest_level

# Schritt 4 – Quest-Ablauf anzeigen
def zeige_quest(quest, belohnung, held_level):
    print(f"--- {quest['name']} ---")
    print(f"Typ: {quest['typ']} | Schwierigkeit: {quest['schwierigkeit']}")
    print(f"Belohnung: {belohnung['xp']} XP, {belohnung['gold']} Gold")
    if pruefe_voraussetzung(held_level, quest["schwierigkeit"]):
        print(f"Status: Verfügbar (Level {held_level} reicht)")
    else:
        mindest = quest["schwierigkeit"] * 2
        print(f"Status: Gesperrt (Mindest-Level: {mindest})")
    print()

# Quests anlegen und anzeigen
held_level = 5
quests = [
    erstelle_quest("Wolfsjagd", "Kampf", 2),
    erstelle_quest("Verlorene Karte", "Erkundung", 3),
    erstelle_quest("Drachenpost", "Lieferung", 1),
]

print(f"=== QUEST-LISTE (Held Level {held_level}) ===")
for q in quests:
    belohnung = berechne_belohnung(q["schwierigkeit"], q["typ"])
    zeige_quest(q, belohnung, held_level)

# Bonus – zufällige Quest
zufall_quest = random.choice(quests)
print(f"Zufällige Quest: {zufall_quest['name']}")