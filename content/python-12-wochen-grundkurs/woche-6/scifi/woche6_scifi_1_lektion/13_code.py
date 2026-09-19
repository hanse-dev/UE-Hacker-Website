# Beispiel 3: Fortgeschrittene Listen-Operationen
mission_typen = ["Forschung", "Verteidigung", "Erforschung", "Forschung", "Verteidigung"]

print("=== Fortgeschrittene Operationen ===")
print(f"Missionstypen-Liste: {mission_typen}")

# Einzigartige Elemente (mit set)
einzigartige_typen = list(set(mission_typen))
print(f"Einzigartige Missionstypen: {einzigartige_typen}")

# Listen mit for-Schleife durchlaufen
print("\nAlle Missionstypen:")
for i, m in enumerate(mission_typen):
    print(f"  Position {i}: {m}")