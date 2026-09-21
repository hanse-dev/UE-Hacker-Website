with open("quest_log.txt", "w") as f:
    f.write("Pyralia Quest-Log\n")
    f.write("Status: Aktiv\n")
    f.write("Monster besiegt\n")
with open("quest_log.txt", "a") as f:
    f.write("Update: Schatz gefunden\n")
with open("quest_log.txt", "r") as f:
    zeilen = f.readlines()
print(f"Zeilen: {len(zeilen)}")
print(f"Letzte: {zeilen[-1].strip()}")
