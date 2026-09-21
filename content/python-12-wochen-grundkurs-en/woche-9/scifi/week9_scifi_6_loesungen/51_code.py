with open("ship_log.txt", "w") as f:
    f.write("Ship log Nebula-7\n")
    f.write("Status: Active\n")
    f.write("Signal received\n")
with open("ship_log.txt", "a") as f:
    f.write("Update: Probe launched\n")
with open("ship_log.txt", "r") as f:
    lines = f.readlines()
print(f"Lines: {len(lines)}")
print(f"Last: {lines[-1].strip()}")
