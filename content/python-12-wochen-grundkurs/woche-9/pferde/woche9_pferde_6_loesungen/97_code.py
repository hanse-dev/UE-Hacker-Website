datum = "15.03."
with open("tagebuch.txt", "w") as f:
    f.write(datum + " Sturm gestriegelt\n")
    f.write(datum + " Ausritt zum Wald\n")
    f.write(datum + " Sprungtraining geschafft\n")

eintrag = input()
with open("tagebuch.txt", "a") as f:
    f.write(datum + " " + eintrag + "\n")

with open("tagebuch.txt") as f:
    zeilen = f.readlines()
print(f"Einträge: {len(zeilen)}")
