import os

with open("ship_log.txt", "w") as f:
    f.write("Ship log Nebula-7\n")
print(f"Exists: {os.path.exists('ship_log.txt')}")
os.remove("ship_log.txt")
print(f"Exists: {os.path.exists('ship_log.txt')}")
