with open("ship_log.txt", "w") as f:
    f.write("Ship log Nebula-7\n")
    f.write("Status: Active\n")
    f.write("Signal received\n")
with open("ship_log.txt", "r") as f:
    lines = f.readlines()
print(f"Lines: {len(lines)}")
print(f"First: {lines[0].strip()}")
