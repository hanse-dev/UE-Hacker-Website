with open("liste.txt", "w") as f:
    f.write("Nova,4\n")
    f.write("Rex,6\n")
    f.write("Zara,3\n")
with open("liste.txt", "r") as f:
    for zeile in f:
        teile = zeile.strip().split(",")
        print(f"{teile[0]}: {teile[1]}")
