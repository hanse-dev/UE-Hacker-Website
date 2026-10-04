datum = "15.03."
with open("tagebuch.txt", "w") as f:
    f.write(datum + " Drachenhöhle betreten\n")
    f.write(datum + " Goldkrone gefunden\n")
    f.write(datum + " Troll besiegt\n")

eintrag = input()
with open("tagebuch.txt", "a") as f:
    f.write(datum + " " + eintrag + "\n")

with open("tagebuch.txt") as f:
    zeilen = f.readlines()
print(f"Einträge: {len(zeilen)}")
