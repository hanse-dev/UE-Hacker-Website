with open("ship_log.txt", "w") as f:
    f.write("Ship log Nebula-7\n")
    f.write("Status: Active\n")
    f.write("Signal received\n")
with open("ship_log.txt", "r") as f:
    content = f.read()
count = content.count("\n")
print(f"Lines: {count}")
