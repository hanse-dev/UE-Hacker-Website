# Beispiel 3: Fortgeschrittene Zufallsfunktionen
import random
import math

print("=== Fortgeschrittene Zufallsfunktionen ===")

# Normalverteilung für Energiewerte
print("Energieverbrauch (Normalverteilung):")
for i in range(5):
    energie = random.gauss(100, 20)  # Mittelwert 100, Stdabw 20
    print(f"  System {i+1}: {max(0, energie):.1f} MW")

# Exponentialverteilung für Wartezeiten
print("\nWartezeiten (Exponentialverteilung):")
for i in range(5):
    warten = random.expovariate(0.1)  # Lambda = 0.1
    print(f"  Wartezeit {i+1}: {warten:.1f} Minuten")

# Zufälliger Punkt im Kreis
def zufalls_punkt_kreis(radius):
    winkel = random.uniform(0, 2 * math.pi)
    r = radius * math.sqrt(random.random())
    x = r * math.cos(winkel)
    y = r * math.sin(winkel)
    return x, y

x, y = zufalls_punkt_kreis(10)
print(f"\nZufälliger Punkt im Kreis r=10: ({x:.2f}, {y:.2f})")