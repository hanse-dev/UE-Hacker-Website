world = {
    "entrance": {
        "description": "You stand at the entrance of the dragon cave. It smells of smoke.",
        "exits": {"north": "hall"},
    },
    "hall": {
        "description": "A huge hall. Torches flicker on the walls.",
        "exits": {"south": "entrance", "east": "treasury", "west": "spring"},
    },
    "spring": {"description": "A quiet spring. The water sparkles magically.", "exits": {"east": "hall"}},
    "treasury": {"description": "Gold as far as you can see – and in the middle sleeps the dragon!", "exits": {"west": "hall"}},
}

def describe(room_name):
    room = world[room_name]
    print(f"📍 {room_name.capitalize()}: {room['description']}")
    print("   Exits:", ", ".join(room["exits"]))

def go(position, direction):
    exits = world[position]["exits"]
    if direction in exits:
        new_position = exits[direction]
        describe(new_position)
        return new_position
    print("🚫 You can't go that way!")
    return position

position = "entrance"
for command in ["north", "east"]:
    position = go(position, command)
print(f"Position: {position}")
