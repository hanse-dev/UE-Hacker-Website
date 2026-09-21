module = ["Antrieb", "Sensor", "Schild", "Radar", "Funk"]
for eintrag in module:
    if eintrag == "Sensor":
        continue
    print(f"- {eintrag}")
