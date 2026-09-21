def calculate_hoof_points(laps, points_per_lap):
    return laps * points_per_lap

points = calculate_hoof_points(4, 15)
print(f"Hoof points: {points}")
