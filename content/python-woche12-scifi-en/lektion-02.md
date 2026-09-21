# 🚀 Stage 2: Moving Around

*Knowledge from week 3–5: conditions, loops, functions*

Now the game starts to move. `go()` checks with `if ... in ...` whether there is an exit in that direction:

```python
def go(position, direction):
    exits = world[position]["exits"]
    if direction in exits:
        new_position = exits[direction]
        describe(new_position)
        return new_position
    print("🚫 You can't go that way!")
    return position
```

- Yes → the new room is returned (`return`) and described
- No → a message appears and the position stays the same

A `for` loop plays a list of commands.
