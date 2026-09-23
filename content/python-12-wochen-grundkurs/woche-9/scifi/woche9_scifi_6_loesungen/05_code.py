with open("bordbuch.txt", "w") as f:
    f.write("Bordbuch Nebula-7\n")
    f.write("Status: Aktiv\n")
    f.write("Signal empfangen\n")
with open("bordbuch.txt", "r") as f:
    inhalt = f.read()
anzahl = inhalt.count("\n")
print(f"Zeilen: {anzahl}")
