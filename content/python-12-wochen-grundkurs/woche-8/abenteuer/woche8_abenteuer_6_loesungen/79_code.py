def erstelle_held(name, art, stufe):
    return {"name": name, "klasse": art, "level": stufe}

held = erstelle_held("Aria", "Magierin", 15)
print(f"Erstellt: {held['name']}")
print(f"Level: {held['level']}")
