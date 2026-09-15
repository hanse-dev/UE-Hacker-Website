import random
import string
import time

# random module
roll = random.randint(1, 6)
print("Dice roll:", roll)

heroes = ["Aria", "Borin", "Lena"]
print("Randomly chosen:", random.choice(heroes))

random.shuffle(heroes)
print("Shuffled:", heroes)

# string module
rune = random.choice(string.ascii_letters)
print("Random rune:", rune)

# time module
print("Casting spell...")
time.sleep(1)
print("Done!")
