# Beispiel 2: Elemente entfernen
futter_plan = ["Heu", "Hafer", "Müsli", "Karotten", "Äpfel", "Müsli"]
print(f"Original-Futterplan: {futter_plan}")

# Mit remove() erstes Vorkommen entfernen
futter_plan.remove("Müsli")
print(f"Nach remove('Müsli'): {futter_plan}")

# Mit pop() letztes Element entfernen und zurückgeben
letztes_futter = futter_plan.pop()
print(f"Nach pop(): {futter_plan}")
print(f"Entferntes Futter: {letztes_futter}")

# Mit pop(index) bestimmtes Element entfernen
zweites_futter = futter_plan.pop(1)
print(f"Nach pop(1): {futter_plan}")
print(f"Entferntes Futter: {zweites_futter}")

# Mit clear() alles löschen
futter_plan.clear()
print(f"Nach clear(): {futter_plan}")