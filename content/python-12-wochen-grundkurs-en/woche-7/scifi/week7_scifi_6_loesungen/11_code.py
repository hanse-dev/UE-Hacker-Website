modules = ["Navigation", "Communication", "Drive", "Life support", "Sensors"]
import random

chosen = random.choice(modules)
print(f"Contained: {chosen in modules}")
