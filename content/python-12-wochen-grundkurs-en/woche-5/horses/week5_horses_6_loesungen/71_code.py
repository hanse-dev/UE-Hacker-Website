def run_lap(distance, speed):
    remaining = distance - speed
    if remaining < 0:
        return 0
    return remaining
def simulate_race(distance, speed, laps):
    for lap in range(1, laps + 1):
        distance = run_lap(distance, speed)
        print(f"Lap {lap}: {distance} m to go")
    return distance

left = simulate_race(100, 30, 4)
print(f"Left: {left}")
