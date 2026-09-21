with open("ship_log.txt", "w") as f:
    f.write("Ship log Nebula-7\n")
    f.write("Status: Active\n")
    f.write("Signal received\n")
def count_lines(name):
    try:
        with open(name, "r") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0

print(f"ship_log.txt: {count_lines('ship_log.txt')}")
print(f"missing.txt: {count_lines('missing.txt')}")
