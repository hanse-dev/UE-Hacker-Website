best_distance = 0
for fuel_use in range(10, 31, 10):
    fuel = 100
    shield = 60
    distance = 0
    while fuel > 0 and shield > 0:
        distance += 1
        fuel -= fuel_use
        shield -= 8
    if distance > best_distance:
        best_distance = distance
print(f"Best distance: {best_distance}")
