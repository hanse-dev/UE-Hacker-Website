zahlen = []
for zahl in range(1, 21):
    zahlen.append(zahl)
print(f"Anzahl: {len(zahlen)}")
print(zahlen[1::2])
print(sorted(zahlen, reverse=True)[:5])
