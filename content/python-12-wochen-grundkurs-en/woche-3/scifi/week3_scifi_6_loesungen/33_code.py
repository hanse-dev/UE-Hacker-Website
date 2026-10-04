sector_safe = True
fuel = 15
if sector_safe:
    if fuel >= 20:
        print("Jump initiated!")
    else:
        print("Refuel!")
else:
    print("Avoid sector!")
