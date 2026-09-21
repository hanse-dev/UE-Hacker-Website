def calculate_power(element, level):
    if element == "FIRE":
        return level * 30
    elif element == "WATER":
        return level * 20
    else:
        return level * 15

print(f"FIRE: {calculate_power('FIRE', 3)}")
print(f"WATER: {calculate_power('WATER', 3)}")
print(f"EARTH: {calculate_power('EARTH', 3)}")
