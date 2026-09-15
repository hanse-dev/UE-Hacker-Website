# Beispiel 2: Elemente entfernen
inventar = ["Schwert", "Schild", "Trank", "Bogen", "Pfeile", "Trank"]
print(f"Original-Inventar: {inventar}")

# Mit remove() erstes Vorkommen entfernen
inventar.remove("Trank")
print(f"Nach remove('Trank'): {inventar}")

# Mit pop() letztes Element entfernen und zurückgeben
letztes_item = inventar.pop()
print(f"Nach pop(): {inventar}")
print(f"Entferntes Item: {letztes_item}")

# Mit pop(index) bestimmtes Element entfernen
zweites_item = inventar.pop(1)
print(f"Nach pop(1): {inventar}")
print(f"Entferntes Item: {zweites_item}")

# Mit clear() alles löschen
inventar.clear()
print(f"Nach clear(): {inventar}")