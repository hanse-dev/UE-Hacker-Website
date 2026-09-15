import math as m
import random as r
import time as t

# Schritt 1: Module ausprobieren
print("=== Nebula-7 Modul-Bank ===")
print(f"math.pi: {m.pi}")
print(f"Zufallszahl (1-10): {r.randint(1, 10)}")

# Schritt 2: Wartezeit-Simulation
wartezeit = r.randint(1, 3)
print(f"\nSystem lädt ... ({wartezeit} Sekunden)")
t.sleep(wartezeit)
print("System bereit!")

# Schritt 3: Flugbahn-Berechnung
winkel_grad = 90
winkel_bogenmass = m.radians(winkel_grad)
flughoehe = m.sin(winkel_bogenmass)
print(f"\nFlugbahn bei {winkel_grad}°: Höhe = {flughoehe:.2f}")

# Schritt 4: Crew-Generator
crew = ["Commander Zara", "Pilot Rex", "Dr. Nova", "Engineer Kai", "Scientist Luna"]
ausgewaehltes_mitglied = r.choice(crew)
print(f"\nAusgewähltes Crew-Mitglied: {ausgewaehltes_mitglied}")

# Bonus: datetime
from datetime import datetime
jetzt = datetime.now()
print(f"Stationszeit: {jetzt.strftime('%H:%M:%S')}")