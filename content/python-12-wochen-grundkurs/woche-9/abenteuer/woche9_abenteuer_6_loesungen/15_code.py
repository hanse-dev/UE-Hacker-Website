import os

with open("quest_log.txt", "w") as f:
    f.write("Pyralia Quest-Log\n")
print(f"Vorhanden: {os.path.exists('quest_log.txt')}")
os.remove("quest_log.txt")
print(f"Vorhanden: {os.path.exists('quest_log.txt')}")
