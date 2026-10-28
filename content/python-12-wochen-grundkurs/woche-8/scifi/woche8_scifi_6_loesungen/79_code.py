def erstelle_mitglied(name, rolle, rang):
    return {"name": name, "rolle": rolle, "rang": rang}

mitglied = erstelle_mitglied("Nova", "Pilotin", 4)
print(f"Erstellt: {mitglied['name']}")
print(f"Rang: {mitglied['rang']}")
