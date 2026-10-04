geschwindigkeit = 640
if geschwindigkeit >= 800:
    print("Stufe: Hyperantrieb")
elif geschwindigkeit >= 600:
    print("Stufe: Schnellflug")
elif geschwindigkeit >= 400:
    print("Stufe: Reiseflug")
elif geschwindigkeit >= 200:
    print("Stufe: Manövrierflug")
else:
    print("Stufe: Schleichfahrt")