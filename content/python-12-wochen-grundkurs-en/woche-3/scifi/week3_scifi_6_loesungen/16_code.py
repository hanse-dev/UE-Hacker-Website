energy = 45
consumption = 50
if energy >= consumption:
    print(f"Jump possible! Remaining: {energy - consumption}%")
else:
    print(f"Jump impossible! Missing: {consumption - energy}%")
