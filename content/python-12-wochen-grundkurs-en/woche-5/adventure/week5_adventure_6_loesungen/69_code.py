def battle_round(health, damage):
    new_health = health - damage
    if new_health < 0:
        return 0
    return new_health

health = 100
health = battle_round(health, 25)
print(f"Health: {health}")
health = battle_round(health, 25)
print(f"Health: {health}")
