feed = {"Oats": 3, "Hay": 5, "Carrots": 2}
import random

drawn = random.choice(list(feed.keys()))
print(f"Drawn valid: {drawn in feed}")
