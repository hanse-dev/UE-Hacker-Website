import math as m
import random as r
import time as t

# Schritt 1: Werkzeuge ausprobieren
print("=== Reiterhof-Werkzeuge ===")
print(f"math.pi: {m.pi}")
print(f"Zufallszahl (1-10): {r.randint(1, 10)}")

# Schritt 2: Wartezeit-Simulation
wartezeit = r.randint(1, 3)
print(f"\nWarte auf Pferd ... ({wartezeit} Sekunden)")
t.sleep(wartezeit)
print("Pferd ist bereit!")

# Schritt 3: Sprung-Berechnung
winkel_grad = 90
winkel_bogenmass = m.radians(winkel_grad)
sprungh_oehe = m.sin(winkel_bogenmass)
print(f"\nSprunghöhe bei {winkel_grad}°: {sprungh_oehe:.2f} m")

# Schritt 4: Reiter-Generator
reiter = ["Lena", "Tom", "Sophie", "Max", "Clara"]
ausgewaehlter_reiter = r.choice(reiter)
print(f"\nAusgewählter Reiter: {ausgewaehlter_reiter}")

# Bonus: datetime
from datetime import datetime
jetzt = datetime.now()
print(f"Trainingszeit: {jetzt.strftime('%H:%M:%S')}")