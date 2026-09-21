def create_compartments(count, spots):
    compartments = []
    for _nr in range(count):
        compartment = []
        for _spot in range(spots):
            compartment.append("empty")
        compartments.append(compartment)
    return compartments
def place(compartments, index, name):
    compartment = compartments[index]
    for spot in range(len(compartment)):
        if compartment[spot] == "empty":
            compartment[spot] = name
            break

compartments = create_compartments(3, 2)
place(compartments, 1, "Chip")
place(compartments, 1, "Cable")
print(compartments)
