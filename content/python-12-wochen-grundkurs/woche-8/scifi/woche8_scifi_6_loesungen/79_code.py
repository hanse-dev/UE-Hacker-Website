def erstelle_mitglied(name, art, stufe):
    return {"name": name, "rolle": art, "rang": stufe}

mitglied = erstelle_mitglied("Nova", "Pilotin", 4)
print(f"Erstellt: {mitglied['name']}")
print(f"Rang: {mitglied['rang']}")
