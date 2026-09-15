# Beispiel 3: Mehrere Module importieren
import math
import random
import time

# Berechne eine zufällige Reitdauer
distanz = 1000  # Meter
geschwindigkeit = random.uniform(0.1, 0.9)  # Bruchteil der Maximalgeschwindigkeit
reitzeit = distanz / geschwindigkeit

print("=== Reit-Simulation ===")
print(f"Distanz: {distanz} Meter")
print(f"Geschwindigkeit: {geschwindigkeit:.2f} m/s")
print(f"Reitzeit: {reitzeit:.1f} Minuten")
print(f"Warte 2 Sekunden...")
time.sleep(2)
print(f"Ankunft am Ziel!")