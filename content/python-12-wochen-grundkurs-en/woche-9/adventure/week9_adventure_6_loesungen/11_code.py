with open("quest_log.txt", "w") as f:
    f.write("Pyralia Quest Log\n")
    f.write("Status: Active\n")
    f.write("Monster defeated\n")
with open("quest_log.txt", "r") as f:
    lines = f.readlines()
print(f"Lines: {len(lines)}")
print(f"First: {lines[0].strip()}")
