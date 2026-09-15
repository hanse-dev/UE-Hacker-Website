# Schritt 1: Übungsliste
uebungen = ["Dressur", "Springen", "Galopp", "Trab", "Schritt"]
print(uebungen)
print(f"Anzahl Übungen: {len(uebungen)}")

# Schritt 2: Hinzufügen & entfernen
uebungen.append("Voltigieren")
uebungen.insert(0, "Aufwärmen")
abgeschlossen = uebungen.pop()
print(f"Abgeschlossen: {abgeschlossen}")
print(uebungen)

# Schritt 3: Suchen & sortieren
uebungen.sort()
print(f"Sortiert: {uebungen}")
print(f"'Galopp' ist an Index: {uebungen.index('Galopp')}")