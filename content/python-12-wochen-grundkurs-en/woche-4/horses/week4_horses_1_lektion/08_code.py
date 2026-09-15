# 🔍 Exercises with range()

# Exercise 1: Countdown to the start
print("=== Countdown to tournament start ===")
for i in range(5, 0, -1):
    print(f"{i}...")
print("🏇 GO!")

# Exercise 2: Even lane numbers
print("\n=== Even lane numbers ===")
for lane in range(2, 21, 2):
    print(f"Lane {lane}", end=" ")
print()

# Exercise 3: Training rounds
print("\n=== Training rounds ===")
for round_ in range(1, 6):
    print(f"Round {round_}: Trot - Canter - Trot")