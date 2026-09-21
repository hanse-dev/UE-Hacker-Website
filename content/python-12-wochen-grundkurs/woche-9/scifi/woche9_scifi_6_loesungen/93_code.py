import json
wort = "raumstation"
zaehler = {}
for b in wort:
    zaehler[b] = zaehler.get(b, 0) + 1
with open("zaehler.json", "w") as f:
    json.dump(zaehler, f)
with open("zaehler.json", "r") as f:
    geladen = json.load(f)
print(f"a: {geladen['a']}")
