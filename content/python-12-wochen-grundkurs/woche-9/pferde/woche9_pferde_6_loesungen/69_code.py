datum = "15.03."
with open("tagebuch.txt", "w") as f:
    f.write(datum + " Sturm gestriegelt\n")
    f.write(datum + " Ausritt zum Wald\n")
    f.write(datum + " Sprungtraining geschafft\n")
with open("tagebuch.txt", "a") as f:
    f.write(datum + " Hufe ausgekratzt\n")
with open("tagebuch.txt", "r") as f:
    zeilen = f.readlines()
print(f"Einträge: {len(zeilen)}")
print(f"Letzter: {zeilen[-1].strip()}")
