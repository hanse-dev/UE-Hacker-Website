# 🐴 Stage 1: The Map of the World

Welcome, young rider! In eleven weeks you have learned everything a programmer of the **riding ranch** needs. Now you put it all together into a real game: a **text adventure** that you build yourself and can extend later.

**Your mission:** In the middle of the night the little foal has disappeared! Search the riding ranch, collect useful things, chase away the angry goat and bring the foal back!

We build the game in **7 stages**. In every stage a note shows where the knowledge comes from:

| Stage | What you build | Knowledge from |
|---|---|---|
| 1 | The map of the world | Week 8 (dictionaries) |
| 2 | Moving around | Week 3–5 (if, functions) |
| 3 | Items | Week 6 + 10 (lists, classes) |
| 4 | Player and inventory | Week 10 (classes, composition) |
| 5 | Enemy and fight | Week 7 + 11 (random, methods) |
| 6 | Wrong input | Week 8 (try/except) |
| 7 | Saving and finale | Week 9 (JSON, files) |

## 🗺️ Stage 1: The Map of the World

*Knowledge from week 8: dictionaries*

A world consists of rooms with a description and exits. That fits into a **dictionary that contains more dictionaries**: the key is the room name, the value a dictionary with description and exits (direction → next room). The function `describe()` (week 5) looks the room up and prints it with an f-string.



```python
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

describe("yard")
```
