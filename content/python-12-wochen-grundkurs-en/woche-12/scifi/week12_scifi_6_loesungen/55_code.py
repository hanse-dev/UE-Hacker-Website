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

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

world["depot"] = {"description": "A depot full of crates.", "exits": {"up": "corridor"}, "items": [], "enemy": None}
world["corridor"]["exits"]["down"] = "depot"
world["depot"]["items"].append(Item("Cell", "A cell that restores energy."))
print([g.name for g in world["depot"]["items"]])
