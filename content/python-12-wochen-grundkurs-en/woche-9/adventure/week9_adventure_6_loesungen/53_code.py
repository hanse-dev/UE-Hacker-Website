with open("quest_log.txt", "w") as f:
    f.write("Pyralia Quest Log\n")
    f.write("Status: Active\n")
    f.write("Monster defeated\n")
def count_lines(name):
    try:
        with open(name, "r") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0

print(f"quest_log.txt: {count_lines('quest_log.txt')}")
print(f"missing.txt: {count_lines('missing.txt')}")
