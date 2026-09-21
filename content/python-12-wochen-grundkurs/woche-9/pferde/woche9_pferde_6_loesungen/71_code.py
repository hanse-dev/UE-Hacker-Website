datum = "15.03."
with open("tagebuch.txt", "w") as f:
    f.write(datum + " Sturm gestriegelt\n")
    f.write(datum + " Ausritt zum Wald\n")
    f.write(datum + " Sprungtraining geschafft\n")
nummer = 0
with open("tagebuch.txt", "r") as f:
    for zeile in f:
        nummer += 1
        print(f"{nummer}: {zeile.strip()}")
