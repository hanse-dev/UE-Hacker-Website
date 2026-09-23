def read_or_empty(name):
    try:
        with open(name, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

print(f"Empty: {read_or_empty('missing.txt') == ''}")
with open("ship_log.txt", "w") as f:
    f.write("Ship log Nebula-7\n")
print(f"Content: {read_or_empty('ship_log.txt').strip()}")
