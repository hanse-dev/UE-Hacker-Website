# 🚀 Stage 1: The Map of the World

Welcome, technician! In eleven weeks you have learned everything a programmer of **Nebula-7** needs. Now you put it all together into a real game: a **text adventure** that you build yourself and can extend later.

**Your mission:** An emergency has broken out on space station Nebula-7! Explore the station, collect equipment, overcome the broken maintenance robot and shut down the reactor before it is too late!

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

describe("airlock")
```
