wort = "raumstation"
zaehler = {}
for b in wort:
    zaehler[b] = zaehler.get(b, 0) + 1
print(f"a: {zaehler['a']}")
