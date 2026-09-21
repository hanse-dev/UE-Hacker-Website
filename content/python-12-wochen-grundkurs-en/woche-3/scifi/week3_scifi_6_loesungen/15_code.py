energy = 90
consumption = 60
if energy >= consumption:
    print(f"Jump possible! Remaining: {energy - consumption}%")
else:
    print(f"Jump impossible! Missing: {consumption - energy}%")
