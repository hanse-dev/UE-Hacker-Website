with open("list.txt", "w") as f:
    f.write("Aria,15\n")
    f.write("Thorin,18\n")
    f.write("Luna,12\n")
with open("list.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        print(f"{parts[0]}: {parts[1]}")
