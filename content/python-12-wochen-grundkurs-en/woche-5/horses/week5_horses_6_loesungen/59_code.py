def calculate_time_bonus(seconds):
    if seconds <= 60:
        return 20
    elif seconds <= 90:
        return 10
    else:
        return 0

def calculate_total(faults, seconds):
    return 100 - faults * 4 + calculate_time_bonus(seconds)
def show_score(name, faults, seconds):
    print(f"{name}: {calculate_total(faults, seconds)} points")

for faults in range(3):
    show_score("Stormwind", faults, 55)
