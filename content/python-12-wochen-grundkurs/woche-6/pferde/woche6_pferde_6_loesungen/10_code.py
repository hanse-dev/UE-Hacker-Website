# Schritt 1: Pferdeliste anlegen
pferde = ["Thunder", "Luna", "Storm", "Bella", "Midnight"]
print(pferde)

# Schritt 2: Pferde hinzufügen
pferde.append("Silver")
pferde.insert(2, "Star")
print(pferde)

# Schritt 3: Pferd entfernen
pferde.remove("Storm")
print(pferde)

# Schritt 4: Sortieren & suchen
pferde.sort()
print(pferde)
print(f"Anzahl Pferde: {len(pferde)}")
if "Luna" in pferde:
    print(f"Luna ist auf Position {pferde.index('Luna')}")