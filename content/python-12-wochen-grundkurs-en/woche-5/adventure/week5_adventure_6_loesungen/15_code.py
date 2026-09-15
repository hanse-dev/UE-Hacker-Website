import random

# Step 1 – Quest data
def create_quest(name, quest_type, difficulty):
    return {"name": name, "type": quest_type, "difficulty": difficulty}

# Step 2 – Calculate reward
def calculate_reward(difficulty, quest_type):
    type_bonus = {"Combat": 50, "Exploration": 30, "Delivery": 20}
    xp = difficulty * 100 + type_bonus.get(quest_type, 0)
    gold = difficulty * 20 + type_bonus.get(quest_type, 0) // 2
    return {"xp": xp, "gold": gold}

# Step 3 – Check requirements
def check_requirement(hero_level, difficulty):
    min_level = difficulty * 2
    return hero_level >= min_level

# Step 4 – Display quest
def show_quest(quest, reward, hero_level):
    print(f"--- {quest['name']} ---")
    print(f"Type: {quest['type']} | Difficulty: {quest['difficulty']}")
    print(f"Reward: {reward['xp']} XP, {reward['gold']} Gold")
    if check_requirement(hero_level, quest["difficulty"]):
        print(f"Status: Available (Level {hero_level} is enough)")
    else:
        min_lvl = quest["difficulty"] * 2
        print(f"Status: Locked (Minimum level: {min_lvl})")
    print()

hero_level = 5
quests = [
    create_quest("Wolf Hunt", "Combat", 2),
    create_quest("Lost Map", "Exploration", 3),
    create_quest("Dragon Post", "Delivery", 1),
]

print(f"=== QUEST LIST (Hero Level {hero_level}) ===")
for q in quests:
    reward = calculate_reward(q["difficulty"], q["type"])
    show_quest(q, reward, hero_level)

# Bonus – random quest
random_quest = random.choice(quests)
print(f"Random quest: {random_quest['name']}")