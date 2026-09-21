word = "spacestation"
counter = {}
for c in word:
    counter[c] = counter.get(c, 0) + 1
print(f"a: {counter['a']}")
