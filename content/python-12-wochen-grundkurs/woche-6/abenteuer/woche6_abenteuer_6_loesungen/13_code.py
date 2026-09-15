# Schritt 1 – Inventarliste anlegen
inventar = ["Langschwert", "Holzschild", "Heiltrank", "Lederstiefel", "Eisenhelm"]
print("Inventar:", inventar)
print(f"Anzahl Items: {len(inventar)}")

# Schritt 2 – Items hinzufügen
inventar.append("Feuerbogen")
inventar.insert(0, "Magierstab")
print("Nach Ergänzung:", inventar)

# Schritt 3 – Items entfernen und suchen
inventar.remove("Holzschild")
letztes = inventar.pop()
print(f"Entferntes Item (pop): {letztes}")
position = inventar.index("Heiltrank")
print(f"Position von Heiltrank: {position}")
print(f"Enthält Magierstab: {'Magierstab' in inventar}")
print("Aktuelles Inventar:", inventar)

# Schritt 4 – Statistik
print(f"\nAnzahl Items: {len(inventar)}")
print(f"Aktuelles Inventar: {inventar}")
print("Status: Inventar bereit für das Abenteuer!")

# Bonus – Items mit Werten
werte = [200, 150, 50, 90]
item_wert_paare = list(zip(inventar, werte))
item_wert_paare.sort(key=lambda x: x[1], reverse=True)
print("\nInventar sortiert nach Wert:")
for item, wert in item_wert_paare:
    print(f"  {item}: {wert} Gold")