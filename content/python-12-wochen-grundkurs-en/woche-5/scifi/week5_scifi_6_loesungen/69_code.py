def fly_leg(distance, speed):
    remaining = distance - speed
    if remaining < 0:
        return 0
    return remaining

distance = 100
distance = fly_leg(distance, 25)
print(f"Distance: {distance}")
distance = fly_leg(distance, 25)
print(f"Distance: {distance}")
