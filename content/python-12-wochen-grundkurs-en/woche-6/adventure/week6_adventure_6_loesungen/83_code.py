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
place(compartments, 1, "Ruby")
place(compartments, 1, "Crown")
def show_overview(compartments):
    for nr, compartment in enumerate(compartments):
        print(f"Compartment {nr + 1}: {compartment}")
    print(f"Compartments: {len(compartments)}")

show_overview(compartments)
