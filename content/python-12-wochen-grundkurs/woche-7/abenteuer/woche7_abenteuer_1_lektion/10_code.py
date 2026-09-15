# Beispiel: Einen Runen-Schlüssel schmieden
import random
import string

alphabet = string.ascii_letters + string.digits
print(f"Runen-Alphabet ({len(alphabet)} Zeichen): {alphabet}")

# Einzelne Rune ziehen
print(f"\nEine zufällige Rune: {random.choice(alphabet)}")

# Einen ganzen Schlüssel schmieden (8 Runen)
schluessel = "".join(random.choice(alphabet) for _ in range(8))
print(f"Dein Runen-Schlüssel: {schluessel}")
