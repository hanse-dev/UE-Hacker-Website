tools = ["Curry comb", "Hoof pick", "Saddle", "Bridle", "Brush"]
import random

chosen = random.choice(tools)
print(f"Chosen valid: {chosen in tools}")
