def create_compartments(count, spots):
    compartments = []
    for nr in range(count):
        compartment = []
        for spot in range(spots):
            compartment.append("empty")
        compartments.append(compartment)
    return compartments

print(create_compartments(3, 2))
