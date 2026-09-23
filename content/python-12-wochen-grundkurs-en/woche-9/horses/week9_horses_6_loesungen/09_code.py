with open("list.txt", "w") as f:
    f.write("Blitz,8\n")
    f.write("Storm,12\n")
    f.write("Luna,6\n")
with open("list.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        print(f"{parts[0]}: {parts[1]}")
