module = ["Antrieb", "Sensor", "Schild", "Radar", "Funk"]
module.insert(0, "Kern")
module.remove("Radar")
print(f"Erstes: {module[0]}")
print(f"Position: {module.index('Sensor')}")
