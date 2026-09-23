with open("quest_log.txt", "w") as f:
    f.write("Pyralia Quest-Log\n")
    f.write("Status: Aktiv\n")
    f.write("Monster besiegt\n")
with open("quest_log.txt", "r") as f:
    inhalt = f.read()
anzahl = inhalt.count("\n")
erste = inhalt.split("\n")[0]
print(f"Zeilen: {anzahl}")
print(f"Erste: {erste}")
