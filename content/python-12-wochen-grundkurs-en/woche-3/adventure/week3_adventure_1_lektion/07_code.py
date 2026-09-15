# Example 1: Success or failure
roll = 18
if roll >= 15:
    print("⚔️ Critical hit!")
else:
    print("💨 Normal strike")

# Example 2: Age check
age = 17
if age >= 18:
    print("🍺 You may enter.")
else:
    print("🚫 Too young for this tavern.")

# Example 3: Inventory check
gold = 45
cost = 50
if gold >= cost:
    print(f"💰 Purchase successful! Remaining: {gold - cost}")
else:
    print(f"❌ Not enough gold! Missing: {cost - gold}")