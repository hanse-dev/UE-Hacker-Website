with open("quest_log.txt", "w") as f:
    f.write("Pyralia Quest Log\n")
    f.write("Status: Active\n")
with open("quest_log.txt", "a") as f:
    f.write("Monster defeated\n")
with open("quest_log.txt", "r") as f:
    for line in f:
        print(line.strip())
