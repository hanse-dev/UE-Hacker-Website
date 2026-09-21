with open("stallbuch.txt", "w") as f:
    f.write("Stallbuch Reiterhof\n")
    f.write("Status: Geöffnet\n")
with open("stallbuch.txt", "a") as f:
    f.write("Ausritt geplant\n")
with open("stallbuch.txt", "r") as f:
    for zeile in f:
        print(zeile.strip())
