prophecies = ["A new planet awaits you", "The stars are favorable", "Trust the ship computer", "A signal from afar", "Beware of the solar storm", "An old comrade reports in"]
import random
import string

name = "Nova"
rune = random.choice(string.ascii_uppercase)
saying = random.choice(prophecies)
horoscope = f"{name} – {rune}: {saying}"
print(f"Name included: {name in horoscope}")
print(f"Saying included: {saying in horoscope}")
