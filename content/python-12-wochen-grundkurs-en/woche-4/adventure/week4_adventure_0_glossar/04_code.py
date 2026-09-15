# for loop over a list
heroes = ["Aria", "Borin", "Lena"]
for hero in heroes:
    print("Hero:", hero)

# range() – number sequence
for i in range(3):
    print("Round", i)

# while loop
lives = 3
while lives > 0:
    print("Lives:", lives)
    lives = lives - 1

# List basics
party = []
party.append("Mage")
party.append("Warrior")
print(party[0])   # Mage
print(len(party)) # 2