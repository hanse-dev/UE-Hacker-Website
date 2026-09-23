with open("quest_log.txt", "w") as f:
    f.write("Pyralia Quest-Log\n")
with open("quest_log.txt", "r") as f:
    inhalt = f.read()
print(f"Inhalt: {inhalt.strip()}")
