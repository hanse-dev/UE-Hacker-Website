with open("liste.txt", "w") as f:
    f.write("Aria,15\n")
    f.write("Thorin,18\n")
    f.write("Luna,12\n")
with open("liste.txt", "r") as f:
    for zeile in f:
        teile = zeile.strip().split(",")
        print(f"{teile[0]}: {teile[1]}")
