mitglied = {"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120}
entfernt = mitglied.pop("rolle")
print(f"Entfernt: {entfernt}")
del mitglied["energie"]
print(f"Eigenschaften: {len(mitglied)}")
