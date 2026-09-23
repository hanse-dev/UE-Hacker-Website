held = {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120}
entfernt = held.pop("klasse")
print(f"Entfernt: {entfernt}")
del held["leben"]
print(f"Eigenschaften: {len(held)}")
