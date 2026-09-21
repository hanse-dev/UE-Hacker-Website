with open("bordbuch.txt", "w") as f:
    f.write("Bordbuch Nebula-7\n")
    f.write("Status: Aktiv\n")
    f.write("Signal empfangen\n")
with open("bordbuch.txt", "a") as f:
    f.write("Update: Sonde gestartet\n")
with open("bordbuch.txt", "r") as f:
    zeilen = f.readlines()
print(f"Zeilen: {len(zeilen)}")
print(f"Letzte: {zeilen[-1].strip()}")
