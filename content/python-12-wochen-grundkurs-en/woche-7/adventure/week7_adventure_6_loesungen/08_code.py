# Problem: string.ascii_letter doesn't exist (typo, missing 's')
import random
import string
rune = random.choice(string.ascii_letters)
print(f"Drawn rune: {rune}")
