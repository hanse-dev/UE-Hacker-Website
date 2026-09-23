stock = {"Battery": 3, "Cable": 5, "Sensor": 2}
import random

drawn = random.choice(list(stock.keys()))
print(f"Drawn valid: {drawn in stock}")
