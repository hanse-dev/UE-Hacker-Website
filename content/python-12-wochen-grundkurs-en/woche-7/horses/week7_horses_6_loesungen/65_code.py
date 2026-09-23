prophecies = ["Today will be your day", "A tournament win lies ahead", "Keep the reins loose", "The wind carries you", "Reward your horse with a carrot", "A new friend waits in the stable"]
import random

saying = random.choice(prophecies)
print(f"Prophecy valid: {saying in prophecies}")
