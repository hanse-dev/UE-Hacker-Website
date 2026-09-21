module = ["Antrieb", "Sensor", "Schild", "Radar", "Funk"]
for eintrag in module:
    print(f"Prüfe: {eintrag}")
    if eintrag == "Schild":
        print("Gefunden!")
        break
