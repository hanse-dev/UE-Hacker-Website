tools = ["Curry comb", "Hoof pick", "Saddle", "Bridle", "Brush", "Blanket"]
import random

drawn = random.sample(tools, 3)
random.shuffle(drawn)
print(f"Count: {len(drawn)}")
print(f"Different: {len(set(drawn)) == 3}")
