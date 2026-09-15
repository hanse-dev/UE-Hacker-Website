# ✨ Examples of good and bad names

# ✅ Good names (clear and descriptive)
def calculate_shield_efficiency(energy, area):
    """Calculates the efficiency of the shields."""
    return (energy / area) * 100

def find_nearest_dock(ship_position, dock_list):
    """Finds the nearest dock to the current position."""
    return min(dock_list, key=lambda d: abs(d - ship_position))

def is_communication_possible(range_, distance):
    """Checks whether communication is possible."""
    return distance <= range_

# ❌ Bad names (unclear or wrong convention)
# def CalculateShieldEfficiency():  # CamelCase
# def se(e, f):  # Too short, not descriptive
# def shield_calculation():  # Noun first

print("=== Good Function Names in Action ===")
efficiency = calculate_shield_efficiency(1000, 50)
print(f"Shield efficiency: {efficiency}%")

position = 100
docks = [50, 200, 350, 500]
nearest_dock = find_nearest_dock(position, docks)
print(f"Nearest dock: {nearest_dock}")

comm_ok = is_communication_possible(1000, 750)
print(f"Communication possible: {comm_ok}")