import random

# Step 1 – Initialise battle
def initialise_battle(group1, group2):
    return {
        "group1": {"name": group1["name"], "armour": group1["armour"], "health": group1["health"]},
        "group2": {"name": group2["name"], "armour": group2["armour"], "health": group2["health"]},
        "round": 0
    }

# Step 2 – Calculate damage
def calculate_damage(base_damage, armour_strength):
    damage = base_damage - armour_strength / 10
    return max(1, int(damage))

# Step 3 – Execute battle round
def execute_round(status):
    status["round"] += 1
    attacker, defender = ("group1", "group2") if random.random() < 0.5 else ("group2", "group1")
    base = random.randint(15, 35)
    damage = calculate_damage(base, status[defender]["armour"])
    status[defender]["health"] -= damage
    print(f"  Round {status['round']}: {status[attacker]['name']} attacks – {damage} damage!")
    print(f"  {status[defender]['name']} has {max(0, status[defender]['health'])} HP left")

# Step 4 – Control battle
def start_battle(group_a, group_b, max_rounds):
    status = initialise_battle(group_a, group_b)
    print(f"=== BATTLE: {group_a['name']} vs. {group_b['name']} ===")
    for _ in range(max_rounds):
        execute_round(status)
        if status["group1"]["health"] <= 0 or status["group2"]["health"] <= 0:
            break
    print()
    if status["group1"]["health"] > status["group2"]["health"]:
        print(f"Winner: {group_a['name']} ({status['group1']['health']} HP left)")
        print(f"Loser: {group_b['name']}")
    else:
        print(f"Winner: {group_b['name']} ({status['group2']['health']} HP left)")
        print(f"Loser: {group_a['name']}")

heroes = {"name": "Light Guards", "armour": 50, "health": 200}
monsters = {"name": "Shadow Dragon", "armour": 30, "health": 180}
start_battle(heroes, monsters, 10)