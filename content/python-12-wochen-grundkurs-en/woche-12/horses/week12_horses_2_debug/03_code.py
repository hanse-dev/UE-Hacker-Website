room = {"description": "A big hall.", "exits": {"north": "cellar", "east": "tower"}}

direction = "west"
target = room["exits"][direction]
print(f"You go to {target}.")