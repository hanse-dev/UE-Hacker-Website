datum = "15.03."
with open("tagebuch.txt", "w") as f:
    f.write(datum + " Drachenhöhle betreten\n")
    f.write(datum + " Goldkrone gefunden\n")
    f.write(datum + " Troll besiegt\n")
nummer = 0
with open("tagebuch.txt", "r") as f:
    for zeile in f:
        nummer += 1
        print(f"{nummer}: {zeile.strip()}")
