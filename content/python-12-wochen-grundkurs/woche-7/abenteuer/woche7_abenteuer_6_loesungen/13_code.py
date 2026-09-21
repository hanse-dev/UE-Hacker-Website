regale = ["Regal der Elemente", "Regal der Tiere", "Regal der Sterne", "Regal der Schatten", "Regal der Helden"]
import random

gezogen = random.sample(regale, 3)
random.shuffle(gezogen)
print(f"Anzahl: {len(gezogen)}")
print(f"Verschieden: {len(set(gezogen)) == 3}")
