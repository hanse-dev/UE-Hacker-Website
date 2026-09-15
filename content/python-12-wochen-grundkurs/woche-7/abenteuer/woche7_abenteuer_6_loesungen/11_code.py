import random as r
import time as t
import string

# Schritt 1: Die drei Wächter beschwören
print("=== Die drei Wächter ===")
print(f"random.randint(1, 6): {r.randint(1, 6)}")
print(f"len(string.ascii_letters): {len(string.ascii_letters)}")
print(f"time.time(): {t.time():.2f}")

# Schritt 2: Warte-Ritual des Zeit-Wächters
wartezeit = r.uniform(1, 3)
print(f"\nDas Siegel beginnt zu leuchten ... ({wartezeit:.1f} Sekunden)")
t.sleep(wartezeit)
print("Das Siegel leuchtet hell!")

# Schritt 3: Runen-Fragment des Wort-Wächters
fragment = r.choice(string.ascii_letters)
print(f"\nRunen-Fragment gefunden: {fragment}")

# Schritt 4: Siegel öffnen
print(f"\nAlle drei Wächter sind besiegt – das Siegel öffnet sich!")

# Bonus: Zeitstempel
from datetime import datetime
jetzt = datetime.now()
print(f"Geöffnet am: {jetzt.strftime('%d.%m.%Y um %H:%M:%S')}")
