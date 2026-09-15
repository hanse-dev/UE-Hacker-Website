# Beispiel 2: Auf Listenelemente zugreifen
inventar = ["Schwert", "Schild", "Trank", "Bogen", "Pfeile"]

print("=== Inventar-Zugriff ===")
print(f"Gesamtes Inventar: {inventar}")
print(f"Erstes Item: {inventar[0]}")
print(f"Zweites Item: {inventar[1]}")
print(f"Letztes Item: {inventar[-1]}")

# Länge der Liste
print(f"Anzahl Items: {len(inventar)}")

# Slicing (Ausschnitte)
print(f"Erste 3 Items: {inventar[0:3]}")
print(f"Letzte 2 Items: {inventar[-2:]}")