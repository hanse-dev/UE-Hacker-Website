# 🔍 Exercises with comparison operators

# Example 1: = vs == in comparison
rank = 15  # Assignment with =
if rank == 15:  # Comparison with ==
    print("✅ Correct: Rank 15 reached")

# Example 2: All four comparison operators
value = 42
print(f"Value: {value}")
print(f"{value} < 50: {value < 50}")
print(f"{value} <= 42: {value <= 42}")
print(f"{value} > 30: {value > 30}")
print(f"{value} >= 42: {value >= 42}")

# Example 3: Practical application
energy = 85
consumption = 60
if energy > consumption:
    print(f"⚡ Jump possible! Remaining: {energy - consumption}%")
elif energy == consumption:
    print("⚖️ Exactly enough for one jump!")
else:
    print(f"❌ Jump impossible! Missing: {consumption - energy}%")