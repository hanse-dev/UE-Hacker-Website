prophezeiungen = ["Ein neuer Planet wartet auf dich", "Die Sterne stehen günstig", "Traue dem Bordcomputer", "Ein Signal aus der Ferne", "Hüte dich vor dem Sonnensturm", "Ein alter Kamerad meldet sich"]
import random
import string

name = "Nova"
rune = random.choice(string.ascii_uppercase)
spruch = random.choice(prophezeiungen)
horoskop = f"{name} – {rune}: {spruch}"
print(f"Name enthalten: {name in horoskop}")
print(f"Spruch enthalten: {spruch in horoskop}")
