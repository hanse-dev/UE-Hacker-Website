beutel = {"Heiltrank": 3, "Fackel": 5, "Seil": 2}
import random

gezogen = random.choice(list(beutel.keys()))
print(f"Gezogen gültig: {gezogen in beutel}")
