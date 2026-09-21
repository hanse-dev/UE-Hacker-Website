werkzeuge = ["Striegel", "Hufkratzer", "Sattel", "Zaumzeug", "Bürste"]
import random

gezogen = random.sample(werkzeuge, 3)
random.shuffle(gezogen)
print(f"Anzahl: {len(gezogen)}")
print(f"Verschieden: {len(set(gezogen)) == 3}")
