energy = 100
lap = 0
while lap < 6:
    lap += 1
    energy -= 15
    if lap == 3:
        energy += 20
    print(f"Lap {lap}: Energy {energy}")
