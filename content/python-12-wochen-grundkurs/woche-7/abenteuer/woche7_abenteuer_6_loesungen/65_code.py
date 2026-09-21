prophezeiungen = ["Ein Drache wird dich beschützen", "Ein Schatz wartet im Norden", "Vertraue dem Mann mit dem Hut", "Der Mond zeigt dir den Weg", "Hüte dich vor dem dritten Tor", "Ein alter Freund kehrt zurück"]
import random

spruch = random.choice(prophezeiungen)
print(f"Prophezeiung gültig: {spruch in prophezeiungen}")
