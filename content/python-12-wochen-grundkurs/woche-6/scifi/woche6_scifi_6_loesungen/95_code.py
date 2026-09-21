staerken = [80, 55, 95, 40, 70]
summe = 0
for s in staerken:
    summe += s
durchschnitt = summe / len(staerken)
ueber = [s for s in staerken if s > durchschnitt]
print(f"Durchschnitt: {durchschnitt}")
print(ueber)
