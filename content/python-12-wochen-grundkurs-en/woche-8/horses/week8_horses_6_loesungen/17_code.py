feed = {"Oats": 3, "Hay": 5, "Carrots": 2}
total = 0
for amount in feed.values():
    total += amount
print(f"Total: {total}")
print(f"Kinds: {len(feed)}")
