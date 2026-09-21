def calculate_points(jumps, faults):
    return jumps * 10 - faults * 5

def create_start_number(name, number):
    return f"{number}: {name}"
def show_start_card(name, number, jumps, faults):
    print(create_start_number(name, number))
    print(f"Points: {calculate_points(jumps, faults)}")
    print(f"Faults: {faults}")

show_start_card("Stormwind", 7, 8, 2)
