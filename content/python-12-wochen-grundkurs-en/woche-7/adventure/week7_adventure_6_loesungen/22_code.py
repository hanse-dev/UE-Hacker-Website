import random

room_types = ["Treasure Room", "Trap", "Empty Room", "Guard Post", "Altar"]
monster_list = ["Goblin", "Skeleton", "Troll", None, None]  # None = no monster

print("=== RANDOM DUNGEON ===")
monster_count = 0

for i in range(1, 6):
    room_type = random.choice(room_types)
    monster = random.choice(monster_list)
    if monster:
        monster_count += 1
        contents = f"Monster: {monster}"
    else:
        contents = "Safe – no monster"
    print(f"Room {i}: {room_type} | {contents}")

required_lives = (monster_count + 1) // 2
print(f"\nTotal monsters: {monster_count}")
print(f"Required lives: {required_lives}")

print()
print("🎉 Boss Quest complete!")
print("🏆 You have defeated the Archivist of Borrowed Magic!")
print("⭐ Title earned: Master of the Library of Pyralia")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 7!")
print("📚 Next week: Dictionaries and Tuples!")
