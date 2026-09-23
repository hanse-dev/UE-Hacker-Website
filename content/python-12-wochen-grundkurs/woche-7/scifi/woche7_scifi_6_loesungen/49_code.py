module = ["Navigation", "Kommunikation", "Antrieb", "Lebenserhaltung", "Sensoren", "Waffen"]
import random

gezogen = random.sample(module, 3)
random.shuffle(gezogen)
print(f"Anzahl: {len(gezogen)}")
print(f"Verschieden: {len(set(gezogen)) == 3}")
