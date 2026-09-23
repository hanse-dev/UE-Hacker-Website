with open("quest_log.txt", "w") as f:
    f.write("Pyralia Quest-Log\n")
    f.write("Status: Aktiv\n")
with open("quest_log.txt", "a") as f:
    f.write("Monster besiegt\n")
with open("quest_log.txt", "r") as f:
    for zeile in f:
        print(zeile.strip())
