prophecies = ["A dragon will protect you", "A treasure waits in the north", "Trust the man with the hat", "The moon shows you the way", "Beware of the third gate", "An old friend returns"]
import random

saying = random.choice(prophecies)
print(f"Prophecy valid: {saying in prophecies}")
