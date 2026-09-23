stock = {"Battery": 3, "Cable": 5, "Sensor": 2}
total = 0
for amount in stock.values():
    total += amount
print(f"Total: {total}")
print(f"Kinds: {len(stock)}")
