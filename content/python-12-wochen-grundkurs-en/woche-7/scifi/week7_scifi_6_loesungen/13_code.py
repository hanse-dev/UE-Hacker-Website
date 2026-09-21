modules = ["Navigation", "Communication", "Drive", "Life support", "Sensors"]
import random

drawn = random.sample(modules, 3)
random.shuffle(drawn)
print(f"Count: {len(drawn)}")
print(f"Different: {len(set(drawn)) == 3}")
