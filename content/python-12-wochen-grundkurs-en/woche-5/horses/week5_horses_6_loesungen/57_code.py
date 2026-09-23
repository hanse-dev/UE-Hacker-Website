def calculate_time_bonus(seconds):
    if seconds <= 60:
        return 20
    elif seconds <= 90:
        return 10
    else:
        return 0
def calculate_total(faults, seconds):
    return 100 - faults * 4 + calculate_time_bonus(seconds)

print(f"Total: {calculate_total(3, 55)}")
