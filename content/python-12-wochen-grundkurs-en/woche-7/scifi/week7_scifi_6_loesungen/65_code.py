prophecies = ["A new planet awaits you", "The stars are favorable", "Trust the ship computer", "A signal from afar", "Beware of the solar storm", "An old comrade reports in"]
import random

saying = random.choice(prophecies)
print(f"Prophecy valid: {saying in prophecies}")
