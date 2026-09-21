datum = "15.03."
with open("tagebuch.txt", "w") as f:
    f.write(datum + " Drachenhöhle betreten\n")
    f.write(datum + " Goldkrone gefunden\n")
    f.write(datum + " Troll besiegt\n")
with open("tagebuch.txt", "a") as f:
    f.write(datum + " Rast am Lagerfeuer\n")
with open("tagebuch.txt", "r") as f:
    zeilen = f.readlines()
print(f"Einträge: {len(zeilen)}")
print(f"Letzter: {zeilen[-1].strip()}")
