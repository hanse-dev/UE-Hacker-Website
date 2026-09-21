prices = {"Battery": 30, "Cable": 5, "Sensor": 10}
most_expensive = None
for name, price in prices.items():
    if most_expensive is None or price > prices[most_expensive]:
        most_expensive = name
print(f"Most expensive item: {most_expensive} ({prices[most_expensive]})")
