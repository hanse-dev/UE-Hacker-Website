feed = {"Oats": 3, "Hay": 5, "Carrots": 2}
try:
    print(feed["Sugar beet"])
except KeyError:
    print("Not in store: Sugar beet")
