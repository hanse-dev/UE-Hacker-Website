module = ["Navigation", "Kommunikation", "Antrieb", "Lebenserhaltung", "Sensoren"]
import random

gewaehlt = random.choice(module)
print(f"Enthalten: {gewaehlt in module}")
