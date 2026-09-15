# Beispiel 1: Die Türme der Wiederholung
print("=== Die drei Türme werden durchsucht ===")
for turm in range(1, 4):
    print(f"Turm {turm}:")
    for stockwerk in range(1, 3):
        print(f"  Stockwerk {stockwerk} wird durchsucht...")

# Beispiel 2: Ein magisches Muster
print("\n=== Ein Muster aus Sternen ===")
for zeile in range(3):
    for spalte in range(4):
        print("⭐", end=" ")
    print()