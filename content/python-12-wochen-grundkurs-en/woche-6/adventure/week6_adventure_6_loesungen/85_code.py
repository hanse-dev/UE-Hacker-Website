def create_quest(name, goal, difficulty):
    return [name, goal, difficulty]

quests = []
quests.append(create_quest("Dragon Hunt", "Mountain", 4))
print(quests[0])
