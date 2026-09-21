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

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

world["spring"]["items"] = [Item("Sword", "A sharp sword stuck in the stone by the spring.")]
print([g.name for g in world["spring"]["items"]])
