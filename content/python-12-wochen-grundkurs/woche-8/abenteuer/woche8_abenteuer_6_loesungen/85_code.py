wort = "abenteuer"
zaehler = {}
for b in wort:
    zaehler[b] = zaehler.get(b, 0) + 1
print(f"e: {zaehler['e']}")
