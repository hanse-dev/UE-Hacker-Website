prophezeiungen = ["Heute wird dein Tag", "Ein Turniersieg liegt vor dir", "Halte die Zügel locker", "Der Wind trägt dich", "Belohne dein Pferd mit einer Möhre", "Ein neuer Freund wartet im Stall"]
import random

spruch = random.choice(prophezeiungen)
print(f"Prophezeiung gültig: {spruch in prophezeiungen}")
