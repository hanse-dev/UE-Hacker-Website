modules = ["Navigation", "Communication", "Drive", "Life support", "Sensors"]
import random

chosen = random.choice(modules)
print(f"Chosen valid: {chosen in modules}")
