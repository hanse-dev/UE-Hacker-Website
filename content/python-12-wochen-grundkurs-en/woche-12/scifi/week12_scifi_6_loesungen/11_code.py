world = {
    "airlock": {
        "description": "You stand in the airlock. Red warning lights flash and the station hums ominously.",
        "exits": {"north": "corridor"},
    },
    "corridor": {
        "description": "A long corridor with many doors. Emergency lighting bathes everything in red light.",
        "exits": {"south": "airlock", "east": "reactor", "west": "lab"},
    },
    "lab": {"description": "A lab full of equipment. Tools are ready on a table.", "exits": {"east": "corridor"}},
    "reactor": {"description": "The reactor room! The reactor hums – and in front of it stands a broken maintenance robot!", "exits": {"west": "corridor"}},
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

position = "airlock"
for command in ["north", "east"]:
    position = go(position, command)
print(f"Position: {position}")
