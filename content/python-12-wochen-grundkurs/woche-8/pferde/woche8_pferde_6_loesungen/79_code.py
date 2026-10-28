def erstelle_pferd(name, rasse, alter):
    return {"name": name, "rasse": rasse, "alter": alter}

pferd = erstelle_pferd("Blitz", "Hannoveraner", 8)
print(f"Erstellt: {pferd['name']}")
print(f"Alter: {pferd['alter']}")
