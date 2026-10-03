fuel = 10
atmosphere = True
landing_spot = False
if fuel >= 20 or (atmosphere and landing_spot):
    print("Emergency landing possible")
else:
    print("Emergency landing impossible")
