# for loop over a list
horses = ["Bobby", "Lightning", "Moritz"]
for horse in horses:
    print("Horse:", horse)

# range() – number sequence
for i in range(3):
    print("Round", i)

# while loop
feed = 3
while feed > 0:
    print("Feed:", feed, "kg")
    feed = feed - 1

# List basics
stable = []
stable.append("Haflinger")
stable.append("Andalusian")
print(stable[0])   # Haflinger
print(len(stable)) # 2