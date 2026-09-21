datum = "15.03."
eintraege = ["Drachenhöhle betreten", "Goldkrone gefunden", "Troll besiegt"]
with open("tagebuch.txt", "w") as f:
    for eintrag in eintraege:
        f.write(datum + " " + eintrag + "\n")
with open("tagebuch.txt", "r") as f:
    zeilen = f.readlines()
print(f"Einträge: {len(zeilen)}")
print(f"Erste Zeile: {zeilen[0].strip()}")
