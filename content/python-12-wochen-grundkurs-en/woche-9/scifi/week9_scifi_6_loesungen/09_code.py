with open("list.txt", "w") as f:
    f.write("Nova,4\n")
    f.write("Rex,6\n")
    f.write("Zara,3\n")
with open("list.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        print(f"{parts[0]}: {parts[1]}")
