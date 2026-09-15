import random
import string
import time

# random-Modul
wurf = random.randint(1, 6)
print("Würfel:", wurf)

helden = ["Aria", "Borin", "Lena"]
print("Zufällig gewählt:", random.choice(helden))

random.shuffle(helden)
print("Gemischt:", helden)

# string-Modul
rune = random.choice(string.ascii_letters)
print("Zufällige Rune:", rune)

# time-Modul
print("Zauber wird gewirkt...")
time.sleep(1)
print("Fertig!")
