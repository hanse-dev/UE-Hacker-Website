quests = [["Dragon Hunt", "Mountain", 4], ["Treasure Hunt", "Cave", 2], ["Riddle Forest", "Forest", 3]]
def search_quests(items, term):
    found = []
    for quest in items:
        if term in quest[0]:
            found.append(quest)
    return found

hits = search_quests(quests, "Hunt")
print(f"Found: {len(hits)}")
