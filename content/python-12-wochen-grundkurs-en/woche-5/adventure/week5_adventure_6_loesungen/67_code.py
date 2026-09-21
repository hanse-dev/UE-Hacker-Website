def calculate_damage(base, armor):
    damage = base - armor
    if damage < 0:
        return 0
    return damage

print(f"Damage: {calculate_damage(40, 15)}")
print(f"Damage: {calculate_damage(10, 30)}")
