def calculate_maintenance(hours):
    return hours * 5

def is_serviceable(energy, duration):
    return energy >= duration * 2
def show_maintenance(ship, energy, hours):
    duration = calculate_maintenance(hours)
    if is_serviceable(energy, duration):
        print(f"{ship}: maintenance {duration} minutes")
    else:
        print(f"{ship}: needs recharge")

show_maintenance("Nebula", 90, 8)
show_maintenance("Comet", 60, 8)
