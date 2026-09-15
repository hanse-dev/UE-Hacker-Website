# Beispiel 3: Komplexe Strukturen
# Artefakt (Tupel) als Steckbrief-Schlüssel
schatz_karte = {
    (100, 200): "Goldtruhe",
    (300, 400): "Magie-Truhe",
    (500, 600): "Artefakt-Truhe"
}

print("=== Schatz-Karte (Tupel als Schlüssel) ===")
for position, schatz in schatz_karte.items():
    print(f"{position}: {schatz}")

# Komplexes Questsystem
quests = {
    "aktiv": [
        {
            "id": 1,
            "ziel": "Drache besiegen",
            "belohnung": ("Gold", 1000, "XP", 500),
            "status": "In Bearbeitung"
        }
    ],
    "abgeschlossen": [
        {
            "id": 2,
            "ziel": "Schatz finden",
            "belohnung": ("Silber", 500, "XP", 250),
            "status": "Erfolg"
        }
    ]
}

print(f"\nAktive Quests: {len(quests['aktiv'])}")
print(f"Abgeschlossene Quests: {len(quests['abgeschlossen'])}")