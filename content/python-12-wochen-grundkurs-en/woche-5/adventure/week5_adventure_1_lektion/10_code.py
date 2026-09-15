# 🔍 Exercises with return

# Example 1: Simple calculation with return
def calculate_damage(base_damage, multiplier):
    """Calculates the total damage of an attack"""
    total_damage = base_damage * multiplier
    return total_damage

# Store result in variable
print("=== Damage Calculation ===")
damage1 = calculate_damage(10, 2)
print(f"Strike 1: {damage1} damage")

damage2 = calculate_damage(15, 3)
print(f"Strike 2: {damage2} damage")

# Use result directly
print(f"Critical hit: {calculate_damage(20, 5)} damage")