def calculate_points(jumps, faults):
    return jumps * 10 - faults * 5

print(f"Points: {calculate_points(8, 2)}")
