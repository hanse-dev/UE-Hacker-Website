lager = {"Batterie": 3, "Kabel": 5, "Sensor": 2}
import random

gezogen = random.choice(list(lager.keys()))
print(f"Gezogen gültig: {gezogen in lager}")
