import json
word = "spacestation"
counter = {}
for c in word:
    counter[c] = counter.get(c, 0) + 1
with open("counter.json", "w") as f:
    json.dump(counter, f)
with open("counter.json", "r") as f:
    loaded = json.load(f)
print(f"a: {loaded['a']}")
