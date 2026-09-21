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

import json
text = json.dumps(world)
back = json.loads(text)
print(back == world)
