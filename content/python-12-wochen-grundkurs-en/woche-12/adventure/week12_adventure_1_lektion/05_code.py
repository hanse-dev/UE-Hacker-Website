# Stage 2: Moving through the world
def go(position, direction):
    exits = world[position]["exits"]
    if direction in exits:
        new_position = exits[direction]
        describe(new_position)
        return new_position
    print("🚫 You can't go that way!")
    return position

position = "entrance"
for command in ["north", "east", "north", "west", "west"]:
    print(f"\n> {command}")
    position = go(position, command)