# 🔍 Übungen mit range()

# Übung 1: Countdown zum Sprung
print("=== Countdown zum Hypersprung ===")
for i in range(5, 0, -1):
    print(f"{i}...")
print("🚀 HYPERSPRUNG!")

# Übung 2: Gerade Zeitstempel
print("\n=== Gerade Zeitstempel ===")
for zeit in range(0, 21, 2):
    print(f"T{zeit:02d}", end=" ")
print()

# Übung 3: Energie-Zyklen
print("\n=== Energie-Zyklen ===")
for zyklus in range(1, 6):
    print(f"Zyklus {zyklus}: Energie-Wellen aktiv")