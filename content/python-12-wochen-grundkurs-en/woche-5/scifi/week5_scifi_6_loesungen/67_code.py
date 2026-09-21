def calculate_speed(base, ballast):
    speed = base - ballast
    if speed < 0:
        return 0
    return speed

print(f"Speed: {calculate_speed(40, 15)}")
print(f"Speed: {calculate_speed(10, 30)}")
