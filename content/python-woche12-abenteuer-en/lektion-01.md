# ⚔️ Stage 1: The Map of the World

Welcome, young mage! In eleven weeks you have learned everything a programmer of the **Guild of Pyralia** needs. Now you put it all together into a real game: a **text adventure** that you build yourself and can extend later.

**Your mission:** Explore the dragon cave, collect items, defeat the dragon and find the treasure of Pyralia!

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

describe("entrance")
```
