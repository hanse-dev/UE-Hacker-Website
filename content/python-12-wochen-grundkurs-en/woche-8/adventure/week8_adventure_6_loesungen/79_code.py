def create_hero(name, kind, level):
    return {"name": name, "class": kind, "level": level}

hero = create_hero("Aria", "Mage", 15)
print(f"Created: {hero['name']}")
print(f"Level: {hero['level']}")
