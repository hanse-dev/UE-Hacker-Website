# Stage 1: The map of the world as a dictionary
world = {
    "yard": {
        "description": "You are standing in the yard. The moon is shining, and you hear a soft neigh from the stable.",
        "exits": {"north": "aisle"},
    },
    "aisle": {
        "description": "A long stable aisle. The horses' boxes stand on the left and right.",
        "exits": {"south": "yard", "east": "paddock", "west": "tackroom"},
    },
    "tackroom": {
        "description": "The tack room smells of leather. Saddles and bridles hang on the wall.",
        "exits": {"east": "aisle"},
    },
    "paddock": {
        "description": "The paddock at night. The foal stands in the grass – and in front of it an angry billy goat!",
        "exits": {"west": "aisle"},
    },
}

def describe(room_name):
    room = world[room_name]
    print(f"📍 {room_name.capitalize()}: {room['description']}")
    print("   Exits:", ", ".join(room["exits"]))

describe("yard")