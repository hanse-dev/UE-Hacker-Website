import random
import string

# Step 1: Luck rune from the name
name = input("Your name: ")
luck_rune = "".join(random.choice(string.ascii_uppercase) for _ in range(len(name)))
print(f"\nYour luck rune: {luck_rune}")

# Step 2: Prophecy
prophecies = [
    "An unexpected adventure awaits you.",
    "The wisdom of the ancients will guide you.",
    "A new friend appears on your path.",
    "Great strength lies hidden within you.",
    "Fate smiles upon you today.",
    "Courage will open doors that seemed closed.",
]
prophecy = random.choice(prophecies)

# Step 3: Horoscope
print("\n=== YOUR MAGICAL HOROSCOPE ===")
print(f"Name:       {name}")
print(f"Luck rune:  {luck_rune}")
print(f"Prophecy:   {prophecy}")

# Bonus: probability
probability = round(100 / len(prophecies), 1)
print(f"\nProbability of this prophecy: {probability}%")
