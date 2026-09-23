def battle_round(health, damage):
    new_health = health - damage
    if new_health < 0:
        return 0
    return new_health
def simulate_battle(health, damage, rounds):
    for round_number in range(1, rounds + 1):
        health = battle_round(health, damage)
        print(f"Round {round_number}: Health {health}")
    return health

final = simulate_battle(100, 30, 4)
print(f"Final: {final}")
