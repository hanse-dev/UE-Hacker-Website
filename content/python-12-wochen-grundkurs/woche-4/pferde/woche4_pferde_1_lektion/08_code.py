# 🔍 Übungen mit range()

# Übung 1: Countdown zum Start
print("=== Countdown zum Turnierstart ===")
for i in range(5, 0, -1):
    print(f"{i}...")
print("🏇 LOS!")

# Übung 2: Gerade Bahnnummern
print("\n=== Gerade Bahnnummern ===")
for bahn in range(2, 21, 2):
    print(f"Bahn {bahn}", end=" ")
print()

# Übung 3: Trainingsrunden
print("\n=== Trainingsrunden ===")
for runde in range(1, 6):
    print(f"Runde {runde}: Trab - Galopp - Trab")