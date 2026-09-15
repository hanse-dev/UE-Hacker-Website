# 🔍 Exercises for comparison operators

# Example 1: = vs == in comparison
age = 8  # Assignment with =
if age == 8:  # Comparison with ==
    print("✅ Correct: The horse is 8 years old")

# Example 2: All four comparison operators
height = 160  # cm at the withers
print(f"Height at withers: {height} cm")
print(f"{height} < 165: {height < 165}")
print(f"{height} <= 160: {height <= 160}")
print(f"{height} > 150: {height > 150}")
print(f"{height} >= 160: {height >= 160}")

# Example 3: Practical application
hay = 25
need = 20
if hay > need:
    print(f"🌾 Enough hay! Leftover: {hay - need} kg")
elif hay == need:
    print("⚖️ Perfect amount!")
else:
    print(f"❌ Not enough hay! Missing: {need - hay} kg")
