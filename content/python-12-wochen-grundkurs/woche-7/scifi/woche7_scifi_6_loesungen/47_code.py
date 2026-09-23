module = ["Navigation", "Kommunikation", "Antrieb", "Lebenserhaltung", "Sensoren"]
import random

gewaehlt = random.choice(module)
print(f"Gewählt gültig: {gewaehlt in module}")
