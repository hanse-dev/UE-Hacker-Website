room = {"description": "A big hall.", "exits": {"north": "cellar", "east": "tower"}}

direction = "west"
if direction in room["exits"]:
    target = room["exits"][direction]
    print(f"You go to {target}.")
else:
    print("🚫 You can't go that way!")