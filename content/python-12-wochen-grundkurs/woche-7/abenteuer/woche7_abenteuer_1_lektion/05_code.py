# Beispiel 3: Mehrere Module gemeinsam nutzen
import random
import time

print("=== Der Archivar prüft deine erste Beschwörung ===")
wartezeit = random.uniform(0.5, 1.5)
print(f"Ein Siegel-Zauber beginnt zu wirken ({wartezeit:.1f} Sekunden)...")
time.sleep(wartezeit)
print("Das erste Siegel leuchtet auf!")
