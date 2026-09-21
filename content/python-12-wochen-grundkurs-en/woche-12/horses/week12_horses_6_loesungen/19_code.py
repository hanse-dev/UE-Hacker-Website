world = {
    "yard": {
        "description": "You stand in the yard. The moon is shining, and you hear a soft whinny from the stable.",
        "exits": {"north": "aisle"},
    },
    "aisle": {
        "description": "A long stable aisle. The horses' stalls are on both sides.",
        "exits": {"south": "yard", "east": "paddock", "west": "saddlery"},
    },
    "saddlery": {"description": "The saddlery smells of leather. Saddles and bridles hang on the wall.", "exits": {"east": "aisle"}},
    "paddock": {"description": "The paddock at night. The foal stands in the grass – and in front of it an angry goat!", "exits": {"west": "aisle"}},
}

def describe(room_name):
    room = world[room_name]
    print(f"📍 {room_name.capitalize()}: {room['description']}")
    print("   Exits:", ", ".join(room["exits"]))

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

world["yard"]["items"] = [Item("Flashlight", "It lights up dark corners.")]
world["aisle"]["items"] = []
world["saddlery"]["items"] = [Item("Broom", "A sturdy broom. It helps to chase away the goat.")]
world["paddock"]["items"] = [Item("Foal", "The little foal follows you trustfully.")]

anzahl = 0
for room in world.values():
    anzahl += len(room["items"])
print(f"Count: {anzahl}")
