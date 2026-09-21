stock = {"Battery": 3, "Cable": 5, "Sensor": 2}
try:
    print(stock["Warp core"])
except KeyError:
    print("Not in store: Warp core")
