prophezeiungen = ["Ein Drache wird dich beschützen", "Ein Schatz wartet im Norden", "Vertraue dem Mann mit dem Hut", "Der Mond zeigt dir den Weg", "Hüte dich vor dem dritten Tor", "Ein alter Freund kehrt zurück"]
import random
import string

name = "Aria"
rune = random.choice(string.ascii_uppercase)
spruch = random.choice(prophezeiungen)
horoskop = f"{name} – {rune}: {spruch}"
print(f"Name enthalten: {name in horoskop}")
print(f"Spruch enthalten: {spruch in horoskop}")
