# Example: Forging a rune key
import random
import string

alphabet = string.ascii_letters + string.digits
print(f"Rune alphabet ({len(alphabet)} characters): {alphabet}")

# Draw a single rune
print(f"\nA random rune: {random.choice(alphabet)}")

# Forge a whole key (8 runes)
key = "".join(random.choice(alphabet) for _ in range(8))
print(f"Your rune key: {key}")
