with open("quest_log.txt", "w") as f:
    f.write("Pyralia Quest-Log\n")
    f.write("Status: Aktiv\n")
    f.write("Monster besiegt\n")
def zeilen_zaehlen(name):
    try:
        with open(name, "r") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0

print(f"quest_log.txt: {zeilen_zaehlen('quest_log.txt')}")
print(f"fehlt.txt: {zeilen_zaehlen('fehlt.txt')}")
