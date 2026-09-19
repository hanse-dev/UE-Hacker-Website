fuel = 10
atmosphere = True
landing_spot = True
if fuel >= 20 or (atmosphere and landing_spot):
    print("Emergency landing possible")
else:
    print("Crash")
