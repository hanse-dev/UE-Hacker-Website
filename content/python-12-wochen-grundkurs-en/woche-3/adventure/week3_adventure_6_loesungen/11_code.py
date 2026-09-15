# Step 1 – Access data
age = 16
gold = 5
has_pass = True

# Steps 2 & 3 – Access rule
if age >= 18 or gold >= 10 or has_pass:
    print("Passage allowed! Travel on, hero!")
    # Bonus: toll only without pass
    if not has_pass:
        print("Toll: 1 gold please!")
else:
    print("Passage denied!")
    print("Come back when you are older, richer, or have a pass.")