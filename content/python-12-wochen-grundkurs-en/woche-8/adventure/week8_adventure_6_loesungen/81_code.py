def create_quest(name, difficulty):
    return {"name": name, "difficulty": difficulty, "status": "open"}

quests = []
quests.append(create_quest("Defeat the dragon", 1))
quests.append(create_quest("Find the treasure", 2))
quests.append(create_quest("Save the village", 3))
print(f"Quest count: {len(quests)}")
print(f"Status: {quests[0]['status']}")
