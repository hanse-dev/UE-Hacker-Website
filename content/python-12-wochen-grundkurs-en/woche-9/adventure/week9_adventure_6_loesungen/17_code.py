def read_or_empty(name):
    try:
        with open(name, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

print(f"Empty: {read_or_empty('missing.txt') == ''}")
with open("quest_log.txt", "w") as f:
    f.write("Pyralia Quest Log\n")
print(f"Content: {read_or_empty('quest_log.txt').strip()}")
