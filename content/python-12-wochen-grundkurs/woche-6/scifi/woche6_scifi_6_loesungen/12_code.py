# Schritt 1: Systemliste
systeme = ["Antrieb", "Schild", "Waffen", "Sensoren", "Lebenserhaltung"]
print(systeme)
print(f"Anzahl Systeme: {len(systeme)}")

# Schritt 2: Systeme hinzufügen & entfernen
systeme.append("Kommunikation")
systeme.insert(0, "Notfall-Reaktor")
ausgefallen = systeme.pop(2)
print(f"System ausgefallen: {ausgefallen}")
print(systeme)

# Schritt 3: Suchen & sortieren
systeme.sort()
print(f"Sortiert: {systeme}")
print(f"'Schild' an Index: {systeme.index('Schild')}")