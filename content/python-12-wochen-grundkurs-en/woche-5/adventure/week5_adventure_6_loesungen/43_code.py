def calculate_health(level, class_name):
    if class_name == "Warrior":
        return level * 20
    else:
        return level * 10

print(f"Warrior: {calculate_health(3, 'Warrior')}")
print(f"Mage: {calculate_health(3, 'Mage')}")
