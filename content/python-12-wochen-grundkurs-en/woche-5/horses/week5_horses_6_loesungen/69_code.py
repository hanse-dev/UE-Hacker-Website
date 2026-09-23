def run_lap(distance, speed):
    remaining = distance - speed
    if remaining < 0:
        return 0
    return remaining

distance = 100
distance = run_lap(distance, 25)
print(f"Distance: {distance}")
distance = run_lap(distance, 25)
print(f"Distance: {distance}")
