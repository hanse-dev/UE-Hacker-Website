import random

with open("zahlen.txt", "w") as f:
    for i in range(10):
        f.write(str(random.randint(1, 100)) + "\n")
zahlen = []
with open("zahlen.txt", "r") as f:
    for zeile in f:
        zahlen.append(int(zeile))
alle_ok = True
for z in zahlen:
    if z < 1 or z > 100:
        alle_ok = False
print(f"Anzahl: {len(zahlen)}")
print(f"Alle im Bereich: {alle_ok}")
