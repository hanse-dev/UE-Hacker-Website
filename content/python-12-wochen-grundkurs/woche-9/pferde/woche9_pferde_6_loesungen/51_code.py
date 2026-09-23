with open("stallbuch.txt", "w") as f:
    f.write("Stallbuch Reiterhof\n")
    f.write("Status: Geöffnet\n")
    f.write("Ausritt geplant\n")
with open("stallbuch.txt", "a") as f:
    f.write("Update: Turnier gewonnen\n")
with open("stallbuch.txt", "r") as f:
    zeilen = f.readlines()
print(f"Zeilen: {len(zeilen)}")
print(f"Letzte: {zeilen[-1].strip()}")
