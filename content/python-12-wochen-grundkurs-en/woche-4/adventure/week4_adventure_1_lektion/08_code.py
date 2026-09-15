# 🔍 Exercises with range()

# Exercise 1: countdown
print("=== Countdown from 5 to 1 ===")
for i in range(5, 0, -1):
    print(f"{i}...")
print("🚀 Launch!")

# Exercise 2: Find even numbers
print("\n=== Even numbers up to 20 ===")
for number in range(0, 21, 2):
    print(number, end=" ")
print()

# Exercise 3: Multiples of 3
print("\n=== Multiples of 3 up to 30 ===")
for i in range(3, 31, 3):
    print(f"3 × {i//3} = {i}")