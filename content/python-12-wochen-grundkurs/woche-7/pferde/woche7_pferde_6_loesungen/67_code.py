prophezeiungen = ["Heute wird dein Tag", "Ein Turniersieg liegt vor dir", "Halte die Zügel locker", "Der Wind trägt dich", "Belohne dein Pferd mit einer Möhre", "Ein neuer Freund wartet im Stall"]
import random
import string

name = "Anna"
rune = random.choice(string.ascii_uppercase)
spruch = random.choice(prophezeiungen)
horoskop = f"{name} – {rune}: {spruch}"
print(f"Name enthalten: {name in horoskop}")
print(f"Spruch enthalten: {spruch in horoskop}")
