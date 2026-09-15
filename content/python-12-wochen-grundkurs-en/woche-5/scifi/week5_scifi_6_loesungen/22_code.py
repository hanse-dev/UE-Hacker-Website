import random

def initialise_battle(fleet1, fleet2):
    return {
        "f1": {"name": fleet1["name"], "shield": fleet1["shield"], "hull": fleet1["hull"]},
        "f2": {"name": fleet2["name"], "shield": fleet2["shield"], "hull": fleet2["hull"]},
        "round": 0
    }

def calculate_damage(base_damage, shield_strength):
    damage = base_damage - shield_strength / 10
    return max(1, int(damage))

def execute_round(status):
    status["round"] += 1
    attacker, target = ("f1", "f2") if random.random() < 0.5 else ("f2", "f1")
    base = random.randint(20, 50)
    if random.random() < 0.2:
        base *= 2
        print("  *** SPECIAL WEAPON! ***")
    damage = calculate_damage(base, status[target]["shield"])
    status[target]["hull"] -= damage
    print(f"  Round {status['round']}: {status[attacker]['name']} fires – {damage} damage!")
    print(f"  {status[target]['name']} hull: {max(0, status[target]['hull'])}")

def start_simulation(fleet1, fleet2, max_rounds):
    status = initialise_battle(fleet1, fleet2)
    print(f"=== BATTLE SIMULATION: {fleet1['name']} vs. {fleet2['name']} ===")
    for _ in range(max_rounds):
        execute_round(status)
        if status["f1"]["hull"] <= 0 or status["f2"]["hull"] <= 0:
            break
    print()
    if status["f1"]["hull"] > status["f2"]["hull"]:
        print(f"Winner: {fleet1['name']} (Hull: {status['f1']['hull']})")
        print(f"Loser: {fleet2['name']}")
    else:
        print(f"Winner: {fleet2['name']} (Hull: {status['f2']['hull']})")
        print(f"Loser: {fleet1['name']}")

alpha = {"name": "Alpha Fleet", "shield": 40, "hull": 300}
beta = {"name": "Beta Fleet", "shield": 60, "hull": 250}
start_simulation(alpha, beta, 8)