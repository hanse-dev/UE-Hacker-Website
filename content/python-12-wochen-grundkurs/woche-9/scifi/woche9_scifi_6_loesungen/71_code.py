datum = "Tag 42"
with open("tagebuch.txt", "w") as f:
    f.write(datum + " Signal empfangen\n")
    f.write(datum + " Sonde gestartet\n")
    f.write(datum + " Hülle repariert\n")
nummer = 0
with open("tagebuch.txt", "r") as f:
    for zeile in f:
        nummer += 1
        print(f"{nummer}: {zeile.strip()}")
