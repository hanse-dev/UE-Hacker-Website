with open("stallbuch.txt", "w") as f:
    f.write("Stallbuch Reiterhof\n")
    f.write("Status: Geöffnet\n")
    f.write("Ausritt geplant\n")
with open("stallbuch.txt", "r") as f:
    inhalt = f.read()
anzahl = inhalt.count("\n")
erste = inhalt.split("\n")[0]
print(f"Zeilen: {anzahl}")
print(f"Erste: {erste}")
