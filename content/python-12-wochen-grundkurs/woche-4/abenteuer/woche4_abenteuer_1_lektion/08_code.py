# 🔍 Übungen mit range()

# Übung 1: countdown
print("=== Countdown von 5 bis 1 ===")
for i in range(5, 0, -1):
    print(f"{i}...")
print("🚀 Start!")

# Übung 2: Gerade Zahlen finden
print("\n=== Gerade Zahlen bis 20 ===")
for zahl in range(0, 21, 2):
    print(zahl, end=" ")
print()

# Übung 3: Vielfache von 3
print("\n=== Vielfache von 3 bis 30 ===")
for i in range(3, 31, 3):
    print(f"3 × {i//3} = {i}")