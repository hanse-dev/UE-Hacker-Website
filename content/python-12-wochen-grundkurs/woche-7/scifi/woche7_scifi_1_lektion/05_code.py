# Beispiel 3: Mehrere Module importieren
import math
import random
import time

# Berechne eine zufällige Flugdauer
distanz = 1000  # Lichtjahre
geschwindigkeit = random.uniform(0.1, 0.9)  # Bruchteil der Lichtgeschwindigkeit
flugzeit = distanz / geschwindigkeit

print("=== Raumflug-Simulation ===")
print(f"Distanz: {distanz} Lichtjahre")
print(f"Geschwindigkeit: {geschwindigkeit:.2f}c")
print(f"Flugzeit: {flugzeit:.1f} Jahre")
print(f"Warte 2 Sekunden...")
time.sleep(2)
print(f"Ankunft im Zielsystem!")