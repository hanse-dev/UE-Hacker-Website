energie = 90
verbrauch = 60
if energie >= verbrauch:
    print(f"Sprung möglich! Rest: {energie - verbrauch}%")
else:
    print(f"Sprung unmöglich! Fehlt: {verbrauch - energie}%")