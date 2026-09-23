prophecies = ["A dragon will protect you", "A treasure waits in the north", "Trust the man with the hat", "The moon shows you the way", "Beware of the third gate", "An old friend returns"]
import random
import string

name = "Aria"
rune = random.choice(string.ascii_uppercase)
saying = random.choice(prophecies)
horoscope = f"{name} – {rune}: {saying}"
print(f"Name included: {name in horoscope}")
print(f"Saying included: {saying in horoscope}")
