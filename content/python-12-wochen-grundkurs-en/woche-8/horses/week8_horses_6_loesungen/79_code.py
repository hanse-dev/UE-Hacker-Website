def create_horse(name, kind, level):
    return {"name": name, "breed": kind, "age": level}

horse = create_horse("Blitz", "Hanoverian", 8)
print(f"Created: {horse['name']}")
print(f"Age: {horse['age']}")
