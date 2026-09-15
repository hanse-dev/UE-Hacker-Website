import random
import string
from datetime import datetime

# Schritt 1: Runen-Alphabet
alphabet = string.ascii_letters + string.digits
print(f"Runen-Alphabet ({len(alphabet)} Zeichen)")

# Schritt 2: Runen-Schlüssel schmieden
schluessel = "".join(random.choice(alphabet) for _ in range(8))
print(f"Dein Runen-Schlüssel: {schluessel}")

# Schritt 3: Die richtige Stunde
jetzt = datetime.now()
if 6 <= jetzt.hour < 18:
    print("\nEs ist Tag – die Sonnentore stehen offen.")
else:
    print("\nEs ist Nacht – nur die Mondtore sind geöffnet.")

# Schritt 4: Archiv öffnen
print(f"\nDas Archiv öffnet sich für dich, Runen-Schlüssel {schluessel} akzeptiert!")

# Bonus: reproduzierbarer Schlüssel
random.seed(42)
test_schluessel = "".join(random.choice(alphabet) for _ in range(8))
print(f"\nBonus – reproduzierbarer Test-Schlüssel (Seed 42): {test_schluessel}")
