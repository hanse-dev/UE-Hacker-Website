modules = ["Drive", "Sensor", "Shield", "Radar", "Radio"]
for entry in modules:
    if entry == "Sensor":
        continue
    print(f"- {entry}")
