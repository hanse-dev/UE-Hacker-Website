def calculate_average(values):
    total = 0
    for value in values:
        total += value
    return total / len(values)

print(f"Average: {calculate_average([10, 20, 30, 40])}")
