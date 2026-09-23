with open("liste.txt", "w") as f:
    f.write("Blitz,8\n")
    f.write("Sturm,12\n")
    f.write("Luna,6\n")
with open("liste.txt", "r") as f:
    for zeile in f:
        teile = zeile.strip().split(",")
        print(f"{teile[0]}: {teile[1]}")
