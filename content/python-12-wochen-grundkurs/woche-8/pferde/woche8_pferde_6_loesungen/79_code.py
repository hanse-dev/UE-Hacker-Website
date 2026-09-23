def erstelle_pferd(name, art, stufe):
    return {"name": name, "rasse": art, "alter": stufe}

pferd = erstelle_pferd("Blitz", "Hannoveraner", 8)
print(f"Erstellt: {pferd['name']}")
print(f"Alter: {pferd['alter']}")
