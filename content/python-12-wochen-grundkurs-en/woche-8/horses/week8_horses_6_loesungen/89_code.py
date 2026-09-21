feed = {"Oats": 3, "Hay": 5, "Carrots": 2}
def amount_of(name):
    try:
        return feed[name]
    except KeyError:
        return 0

print(f"Oats: {amount_of('Oats')}")
print(f"Sugar beet: {amount_of('Sugar beet')}")
