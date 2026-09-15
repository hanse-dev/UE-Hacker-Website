# Beispiel 2: Elemente entfernen
system_protokolle = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Gamma"]
print(f"Original-Protokolle: {system_protokolle}")

# Mit remove() erstes Vorkommen entfernen
system_protokolle.remove("Gamma")
print(f"Nach remove('Gamma'): {system_protokolle}")

# Mit pop() letztes Element entfernen und zurückgeben
letztes_protokoll = system_protokolle.pop()
print(f"Nach pop(): {system_protokolle}")
print(f"Entferntes Protokoll: {letztes_protokoll}")

# Mit pop(index) bestimmtes Element entfernen
zweites_protokoll = system_protokolle.pop(1)
print(f"Nach pop(1): {system_protokolle}")
print(f"Entferntes Protokoll: {zweites_protokoll}")

# Mit clear() alles löschen
system_protokolle.clear()
print(f"Nach clear(): {system_protokolle}")