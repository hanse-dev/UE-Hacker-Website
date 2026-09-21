tools = ["Curry comb", "Hoof pick", "Saddle", "Bridle", "Brush"]
import random

chosen = random.choice(tools)
print(f"Contained: {chosen in tools}")
