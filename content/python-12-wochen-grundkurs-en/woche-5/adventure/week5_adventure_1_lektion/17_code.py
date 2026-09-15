# ✨ Examples of good and bad names

# ✅ Good names (clear and descriptive)
def calculate_healing(base_healing, multiplier):
    """Calculates the healing amount."""
    return base_healing * multiplier

def find_max_level(level_list):
    """Finds the highest level in a list."""
    return max(level_list)

def is_quest_available(level, required_level):
    """Checks whether a quest is available."""
    return level >= required_level

# ❌ Bad names (unclear or wrong convention)
# def calculateHealing():  # CamelCase
# def bh(b, m):  # Too short, not descriptive
# def healing_calculation():  # Noun first

print("=== Good Function Names in Action ===")
healing = calculate_healing(10, 2)
print(f"Healing: {healing}")

levels = [5, 8, 12, 3, 15]
max_level = find_max_level(levels)
print(f"Highest level: {max_level}")

quest_ok = is_quest_available(8, 10)
print(f"Quest available: {quest_ok}")