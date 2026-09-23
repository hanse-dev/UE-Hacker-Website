with open("bordbuch.txt", "w") as f:
    f.write("Bordbuch Nebula-7\n")
    f.write("Status: Aktiv\n")
with open("bordbuch.txt", "a") as f:
    f.write("Signal empfangen\n")
with open("bordbuch.txt", "r") as f:
    for zeile in f:
        print(zeile.strip())
