inventar = ["Trank", "Schwert", "Schlüssel", "Schatz", "Karte"]

# break: Suche beenden sobald Schatz gefunden
print("=== Schatzsuche ===")
for gegenstand in inventar:
    print(f"Prüfe: {gegenstand}")
    if gegenstand == "Schatz":
        print("🎉 Schatz gefunden! Suche beendet.")
        break

# continue: Tränke beim Ausgeben überspringen
print("\n=== Inventar ohne Tränke ===")
for gegenstand in inventar:
    if gegenstand == "Trank":
        continue
    print(f"  - {gegenstand}")
