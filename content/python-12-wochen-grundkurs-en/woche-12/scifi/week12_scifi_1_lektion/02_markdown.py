"""## 🗺️ Stage 1: The map of the world

*Knowledge from Week 8: dictionaries*

A space station is made of rooms, and every room has a description and exits. That fits perfectly into a **dictionary that contains more dictionaries**:

- the outer key is the name of the room (e.g. `"corridor"`)
- the inner value is another dictionary with `"description"` and `"exits"`
- the exits are a dictionary themselves: direction → name of the next room

The function `describe()` (Week 5) looks up the room and prints it with an f-string (Week 2)."""