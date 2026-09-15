# Beispiel 1: Die Trainingswochen
print("=== Der Trainingsplan wird durchgegangen ===")
for woche in range(1, 4):
    print(f"Trainingswoche {woche}:")
    for einheit in range(1, 3):
        print(f"  Einheit {einheit} wird absolviert...")

# Beispiel 2: Ein Muster aus Hufabdrücken
print("\n=== Ein Muster aus Hufabdrücken ===")
for zeile in range(3):
    for spalte in range(4):
        print("🐴", end=" ")
    print()