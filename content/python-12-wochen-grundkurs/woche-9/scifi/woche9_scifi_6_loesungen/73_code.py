datum = "Tag 42"
with open("logbuch.txt", "w") as f:
    f.write(datum + " Signal empfangen\n")
    f.write(datum + " Sonde gestartet\n")
    f.write(datum + " Hülle repariert\n")

eintrag = input()
with open("logbuch.txt", "a") as f:
    f.write(datum + " " + eintrag + "\n")

with open("logbuch.txt") as f:
    zeilen = f.readlines()
print(f"Einträge: {len(zeilen)}")
