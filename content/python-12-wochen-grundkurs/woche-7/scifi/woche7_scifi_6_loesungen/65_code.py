prophezeiungen = ["Ein neuer Planet wartet auf dich", "Die Sterne stehen günstig", "Traue dem Bordcomputer", "Ein Signal aus der Ferne", "Hüte dich vor dem Sonnensturm", "Ein alter Kamerad meldet sich"]
import random

spruch = random.choice(prophezeiungen)
print(f"Prophezeiung gültig: {spruch in prophezeiungen}")
