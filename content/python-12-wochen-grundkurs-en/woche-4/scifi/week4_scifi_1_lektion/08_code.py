# 🔍 Exercises with range()

# Exercise 1: Countdown to jump
print("=== Countdown to Hyperspace Jump ===")
for i in range(5, 0, -1):
    print(f"{i}...")
print("🚀 HYPERSPACE JUMP!")

# Exercise 2: Even timestamps
print("\n=== Even Timestamps ===")
for time in range(0, 21, 2):
    print(f"T{time:02d}", end=" ")
print()

# Exercise 3: Energy cycles
print("\n=== Energy Cycles ===")
for cycle in range(1, 6):
    print(f"Cycle {cycle}: Energy waves active")