# Step 1 – Create a quest
def create_quest(name, goal, difficulty):
    return {"name": name, "goal": goal, "difficulty": difficulty, "status": "open"}

# Step 2 – Add quest to list
quests = []

def add_quest(quest, quest_list):
    quest_list.append(quest)
    print(f"Quest '{quest['name']}' added.")

add_quest(create_quest("Wolf Hunt", "Forest of Mirkath", 2), quests)
add_quest(create_quest("Treasure Map", "Lost Ruins", 4), quests)
add_quest(create_quest("Dragon Egg", "Fire Peak", 5), quests)
add_quest(create_quest("Herb Search", "Silver Valley", 1), quests)
add_quest(create_quest("Delivery Errand", "Village Alton", 1), quests)

# Mark quests as completed
quests[0]["status"] = "completed"
quests[3]["status"] = "completed"

# Step 3 – Search quests
def search_quests(quest_list, search_term):
    return [q for q in quest_list if search_term.lower() in q["name"].lower() or search_term.lower() in q["goal"].lower()]

found = search_quests(quests, "Forest")
print(f"\nSearch for 'Forest': {[q['name'] for q in found]}")

# Step 4 – Filter by status
def filter_by_status(quest_list, status):
    return [q for q in quest_list if q["status"] == status]

open_quests = filter_by_status(quests, "open")
completed_quests = filter_by_status(quests, "completed")

# Step 5 – Print statistics
def quest_stats(quest_list):
    print(f"\n=== QUEST STATISTICS ===")
    print(f"Total: {len(quest_list)}")
    print(f"Open: {len(filter_by_status(quest_list, 'open'))}")
    print(f"Completed: {len(filter_by_status(quest_list, 'completed'))}")
    difficulties = {}
    for q in quest_list:
        d = q["difficulty"]
        difficulties[d] = difficulties.get(d, 0) + 1
    print("Difficulty distribution:", difficulties)

quest_stats(quests)

# Bonus – reward field and success statistics
for q in quests:
    q["reward"] = q["difficulty"] * 100

earned_xp = sum(q["reward"] for q in completed_quests)
print(f"\nXP earned from completed quests: {earned_xp}")