datum = "Tag 42"
with open("tagebuch.txt", "w") as f:
    f.write(datum + " Signal empfangen\n")
    f.write(datum + " Sonde gestartet\n")
    f.write(datum + " Hülle repariert\n")
with open("tagebuch.txt", "a") as f:
    f.write(datum + " Energiezelle geladen\n")
with open("tagebuch.txt", "r") as f:
    zeilen = f.readlines()
print(f"Einträge: {len(zeilen)}")
print(f"Letzter: {zeilen[-1].strip()}")
