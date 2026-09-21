modules = ["Drive", "Sensor", "Shield", "Radar", "Radio"]
for entry in modules:
    print(f"Check: {entry}")
    if entry == "Shield":
        print("Found!")
        break
