datum = "Tag 42"
with open("tagebuch.txt", "w") as f:
    f.write(datum + " Signal empfangen\n")
    f.write(datum + " Sonde gestartet\n")
    f.write(datum + " Hülle repariert\n")

eintrag = input()
with open("tagebuch.txt", "a") as f:
    f.write(datum + " " + eintrag + "\n")

with open("tagebuch.txt") as f:
    zeilen = f.readlines()
print(f"Einträge: {len(zeilen)}")
