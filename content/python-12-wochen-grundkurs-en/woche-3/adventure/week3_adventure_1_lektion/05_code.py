# 🔍 Exercises for comparison operators

# Example 1: = vs == compared
level = 15  # assignment with =
if level == 15:  # comparison with ==
    print("✅ Correct: level is 15")

# Example 2: All four comparison operators
value = 10
print(f"Value: {value}")
print(f"{value} < 15: {value < 15}")
print(f"{value} <= 10: {value <= 10}")
print(f"{value} > 5: {value > 5}")
print(f"{value} >= 10: {value >= 10}")

# Example 3: Practical application
gold = 100
cost = 80
if gold > cost:
    print(f"🛍️ Purchase possible! Remaining: {gold - cost}")
elif gold == cost:
    print("💰 Enough for exactly one purchase!")
else:
    print(f"❌ Too expensive! Missing: {cost - gold}")