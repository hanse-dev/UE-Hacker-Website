quests = [["Dragon Hunt", "Mountain", 4], ["Treasure Hunt", "Cave", 2], ["Riddle Forest", "Forest", 3]]
def quest_statistics(items):
    count = 0
    hard = 0
    for quest in items:
        count += 1
        if quest[2] < 3:
            continue
        hard += 1
    print(f"Quests: {count}")
    print(f"Hard quests: {hard}")

quest_statistics(quests)
