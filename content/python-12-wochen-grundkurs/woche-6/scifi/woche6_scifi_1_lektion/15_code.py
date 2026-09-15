schiffe = ["Nebula-Explorer", "Star-Fighter", "Cargo-Hauler", "Science-Vessel"]

# break: Suche beenden sobald das gesuchte Schiff gefunden ist
print("=== Schiffs-Suche ===")
for schiff in schiffe:
    print(f"Prüfe: {schiff}")
    if schiff == "Cargo-Hauler":
        print("🚀 Cargo-Hauler gefunden! Suche beendet.")
        break

# continue: beschädigte Schiffe beim Start überspringen
print("\n=== Startbereite Schiffe ===")
beschaedigt = ["Star-Fighter"]
for schiff in schiffe:
    if schiff in beschaedigt:
        continue
    print(f"  - {schiff} ist startbereit")