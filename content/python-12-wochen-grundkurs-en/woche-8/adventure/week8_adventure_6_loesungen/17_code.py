bag = {"Potion": 3, "Torch": 5, "Rope": 2}
total = 0
for amount in bag.values():
    total += amount
print(f"Total: {total}")
print(f"Kinds: {len(bag)}")
