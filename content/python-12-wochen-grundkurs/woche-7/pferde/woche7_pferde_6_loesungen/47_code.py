werkzeuge = ["Striegel", "Hufkratzer", "Sattel", "Zaumzeug", "Bürste"]
import random

gewaehlt = random.choice(werkzeuge)
print(f"Gewählt gültig: {gewaehlt in werkzeuge}")
