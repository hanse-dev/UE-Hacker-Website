# for-Schleife über eine Liste
crew = ["Kirk", "Spock", "Uhura"]
for mitglied in crew:
    print("Crew:", mitglied)

# range() – Zahlenfolge
for i in range(3):
    print("Runde", i)

# while-Schleife
energie = 3
while energie > 0:
    print("Energie:", energie, "%")
    energie = energie - 1

# Listen-Grundlagen
mannschaft = []
mannschaft.append("Pilot")
mannschaft.append("Navigator")
print(mannschaft[0])   # Pilot
print(len(mannschaft)) # 2
