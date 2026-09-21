pferd = {"name": "Blitz", "rasse": "Hannoveraner", "alter": 8, "punkte": 120}
entfernt = pferd.pop("rasse")
print(f"Entfernt: {entfernt}")
del pferd["punkte"]
print(f"Eigenschaften: {len(pferd)}")
