# Schritt 1 – Quest anlegen
def erstelle_quest(name, ziel, schwierigkeit):
    return {"name": name, "ziel": ziel, "schwierigkeit": schwierigkeit, "status": "offen"}

# Schritt 2 – Quest zur Liste hinzufügen
quests = []

def fuege_quest_hinzu(quest, questliste):
    questliste.append(quest)
    print(f"Quest '{quest['name']}' hinzugefügt.")

fuege_quest_hinzu(erstelle_quest("Wolfsjagd", "Wald von Mirkath", 2), quests)
fuege_quest_hinzu(erstelle_quest("Schatzkarte", "Verlorene Ruinen", 4), quests)
fuege_quest_hinzu(erstelle_quest("Drachen-Ei", "Feuergipfel", 5), quests)
fuege_quest_hinzu(erstelle_quest("Kräutersuche", "Silbertal", 1), quests)
fuege_quest_hinzu(erstelle_quest("Botenauftrag", "Dorf Alton", 1), quests)

# Quest als abgeschlossen markieren
quests[0]["status"] = "abgeschlossen"
quests[3]["status"] = "abgeschlossen"

# Schritt 3 – Quests suchen
def suche_quests(questliste, suchbegriff):
    return [q for q in questliste if suchbegriff.lower() in q["name"].lower() or suchbegriff.lower() in q["ziel"].lower()]

gefunden = suche_quests(quests, "Wald")
print(f"\nSuche nach 'Wald': {[q['name'] for q in gefunden]}")

# Schritt 4 – Nach Status filtern
def filtere_nach_status(questliste, status):
    return [q for q in questliste if q["status"] == status]

offene = filtere_nach_status(quests, "offen")
abgeschlossene = filtere_nach_status(quests, "abgeschlossen")

# Schritt 5 – Statistik ausgeben
def quest_statistik(questliste):
    print(f"\n=== QUEST-STATISTIK ===")
    print(f"Gesamt: {len(questliste)}")
    print(f"Offen: {len(filtere_nach_status(questliste, 'offen'))}")
    print(f"Abgeschlossen: {len(filtere_nach_status(questliste, 'abgeschlossen'))}")
    schwierigkeiten = {}
    for q in questliste:
        s = q["schwierigkeit"]
        schwierigkeiten[s] = schwierigkeiten.get(s, 0) + 1
    print("Schwierigkeitsverteilung:", schwierigkeiten)

quest_statistik(quests)

# Bonus – Belohnungsfeld und Erfolgsstatistik
for q in quests:
    q["belohnung"] = q["schwierigkeit"] * 100

erfolgs_xp = sum(q["belohnung"] for q in abgeschlossene)
print(f"\nGesammelte XP aus abgeschlossenen Quests: {erfolgs_xp}")