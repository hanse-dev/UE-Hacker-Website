def berechne_leben(level, klasse):
    if klasse == "Krieger":
        return level * 20
    else:
        return level * 10

def erstelle_titel(name, klasse):
    return f"{name} der {klasse}"
def zeige_charakterbogen(name, klasse, level):
    print(erstelle_titel(name, klasse))
    print(f"Leben: {berechne_leben(level, klasse)}")
    print(f"Level: {level}")

zeige_charakterbogen("Thorin", "Krieger", 4)
