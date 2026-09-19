# Beispiel 3: Fortgeschrittene Listen-Operationen
disziplinen = ["Dressur", "Springen", "Western", "Dressur", "Western"]

print("=== Fortgeschrittene Operationen ===")
print(f"Disziplinen-Liste: {disziplinen}")

# Einzigartige Elemente (mit set)
einzigartige_disziplinen = list(set(disziplinen))
print(f"Einzigartige Disziplinen: {einzigartige_disziplinen}")

# Listen mit for-Schleife durchlaufen
print("\nAlle Disziplinen:")
for i, d in enumerate(disziplinen):
    print(f"  Position {i}: {d}")