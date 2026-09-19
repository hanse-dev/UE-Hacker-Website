# Stage 1: The map of the world as a dictionary
world = {
    "airlock": {
        "description": "You are standing in the airlock. Red warning lights blink, and the station hums menacingly.",
        "exits": {"north": "corridor"},
    },
    "corridor": {
        "description": "A long corridor with many doors. Emergency lighting bathes everything in red.",
        "exits": {"south": "airlock", "east": "reactor", "west": "lab"},
    },
    "lab": {
        "description": "A lab full of equipment. Tools lie ready on a table.",
        "exits": {"east": "corridor"},
    },
    "reactor": {
        "description": "The reactor room! The reactor hums – and in front of it stands a broken maintenance robot!",
        "exits": {"west": "corridor"},
    },
}

def describe(room_name):
    room = world[room_name]
    print(f"📍 {room_name.capitalize()}: {room['description']}")
    print("   Exits:", ", ".join(room["exits"]))

describe("airlock")