prophecies = ["Today will be your day", "A tournament win lies ahead", "Keep the reins loose", "The wind carries you", "Reward your horse with a carrot", "A new friend waits in the stable"]
import random
import string

name = "Anna"
rune = random.choice(string.ascii_uppercase)
saying = random.choice(prophecies)
horoscope = f"{name} – {rune}: {saying}"
print(f"Name included: {name in horoscope}")
print(f"Saying included: {saying in horoscope}")
