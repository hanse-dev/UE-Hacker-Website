import random
import string
from datetime import datetime

# Step 1: Rune alphabet
alphabet = string.ascii_letters + string.digits
print(f"Rune alphabet ({len(alphabet)} characters)")

# Step 2: Forge the rune key
key = "".join(random.choice(alphabet) for _ in range(8))
print(f"Your rune key: {key}")

# Step 3: The right hour
now = datetime.now()
if 6 <= now.hour < 18:
    print("\nIt is day – the Sun Gates stand open.")
else:
    print("\nIt is night – only the Moon Gates are open.")

# Step 4: Open the archive
print(f"\nThe archive opens for you, rune key {key} accepted!")

# Bonus: reproducible key
random.seed(42)
test_key = "".join(random.choice(alphabet) for _ in range(8))
print(f"\nBonus – reproducible test key (seed 42): {test_key}")
