def fly_leg(distance, speed):
    remaining = distance - speed
    if remaining < 0:
        return 0
    return remaining
def simulate_chase(distance, speed, legs):
    for leg in range(1, legs + 1):
        distance = fly_leg(distance, speed)
        print(f"Leg {leg}: {distance} km to go")
    return distance

left = simulate_chase(100, 30, 4)
print(f"Left: {left}")
