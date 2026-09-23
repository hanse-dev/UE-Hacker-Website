modules = ["Drive", "Sensor", "Shield", "Radar", "Radio"]
modules.insert(0, "Core")
modules.remove("Radar")
print(f"First: {modules[0]}")
print(f"Position: {modules.index('Sensor')}")
