futter = {"Hafer": 3, "Heu": 5, "Möhren": 2}
import random

gezogen = random.choice(list(futter.keys()))
print(f"Gezogen gültig: {gezogen in futter}")
