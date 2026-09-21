stock = {"Battery": 3, "Cable": 5, "Sensor": 2}
def amount_of(name):
    try:
        return stock[name]
    except KeyError:
        return 0

print(f"Battery: {amount_of('Battery')}")
print(f"Warp core: {amount_of('Warp core')}")
