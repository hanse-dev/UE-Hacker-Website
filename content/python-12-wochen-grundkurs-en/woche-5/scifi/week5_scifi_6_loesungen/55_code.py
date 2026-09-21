def calculate_shield_bonus(modules):
    if modules >= 5:
        return 20
    elif modules >= 3:
        return 10
    else:
        return 0

print(f"Bonus: {calculate_shield_bonus(6)}")
print(f"Bonus: {calculate_shield_bonus(4)}")
print(f"Bonus: {calculate_shield_bonus(1)}")
