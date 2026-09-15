# for loop over a list
crew = ["Kirk", "Spock", "Uhura"]
for member in crew:
    print("Crew:", member)

# range() – number sequence
for i in range(3):
    print("Round", i)

# while loop
energy = 3
while energy > 0:
    print("Energy:", energy, "%")
    energy = energy - 1

# List basics
team = []
team.append("Pilot")
team.append("Navigator")
print(team[0])   # Pilot
print(len(team)) # 2