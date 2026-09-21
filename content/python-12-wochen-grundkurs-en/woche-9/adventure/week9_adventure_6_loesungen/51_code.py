with open("quest_log.txt", "w") as f:
    f.write("Pyralia Quest Log\n")
    f.write("Status: Active\n")
    f.write("Monster defeated\n")
with open("quest_log.txt", "a") as f:
    f.write("Update: Treasure found\n")
with open("quest_log.txt", "r") as f:
    lines = f.readlines()
print(f"Lines: {len(lines)}")
print(f"Last: {lines[-1].strip()}")
