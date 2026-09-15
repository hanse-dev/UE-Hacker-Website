# Beispiel 3: Komplexe Archiv-Strukturen
# Kapsel als Stallkarte-Schlüssel
box_karte = {
    (1, 1): "Thunder",
    (1, 2): "Luna",
    (2, 1): "Stormy"
}

print("=== Box-Karte ===")
for position, pferd in box_karte.items():
    print(f"Box {position}: {pferd}")

# Komplexes Trainingssystem
training = {
    "aktiv": [
        {
            "pferd": "Thunder",
            "disziplin": "Dressur",
            "zeitplan": ("Mo", "Mi", "Fr"),
            "status": "In Bearbeitung"
        }
    ],
    "abgeschlossen": [
        {
            "pferd": "Luna",
            "disziplin": "Western",
            "zeitplan": ("Di", "Do"),
            "status": "Erfolg"
        }
    ]
}

print(f"\nAktive Trainings: {len(training['aktiv'])}")
print(f"Abgeschlossene Trainings: {len(training['abgeschlossen'])}")