with open("ship_log.txt", "w") as f:
    f.write("Ship log Nebula-7\n")
    f.write("Status: Active\n")
with open("ship_log.txt", "a") as f:
    f.write("Signal received\n")
with open("ship_log.txt", "r") as f:
    for line in f:
        print(line.strip())
