monsters = ["Goblin", "Orc", "Dragon"]
import random

contents = []
monster_count = 0
for room in range(5):
    if random.randint(0, 1) == 1:
        contents.append(random.choice(monsters))
    else:
        contents.append("empty")
for content in contents:
    if content != "empty":
        monster_count += 1
print(f"Rooms: {len(contents)}")
print(f"Count fits: {0 <= monster_count <= 5}")
