with open("quest_log.txt", "w") as f:
    f.write("Pyralia Quest Log\n")
    f.write("Status: Active\n")
    f.write("Monster defeated\n")
with open("quest_log.txt", "r") as f:
    content = f.read()
count = content.count("\n")
first = content.split("\n")[0]
print(f"Lines: {count}")
print(f"First: {first}")
