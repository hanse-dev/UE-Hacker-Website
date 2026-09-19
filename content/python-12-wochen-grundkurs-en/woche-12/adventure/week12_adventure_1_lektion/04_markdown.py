"""## 🧭 Stage 2: Moving through the world

*Knowledge from Weeks 3–5: conditions, loops, functions*

Now the game starts moving. The function `go()` uses `if ... in ...` to check whether there is an exit in that direction:

- Yes → the new room is returned (`return`) and described
- No → a message appears and the player stays where they are

A `for` loop plays a list of commands one after another. Later the game loop takes over."""