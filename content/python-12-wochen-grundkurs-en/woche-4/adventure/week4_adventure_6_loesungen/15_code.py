import random

# Step 1 – Variables
steps = 0
position = [0, 0]  # [x, y]
exit_position = [0, 0]
directions = ["North", "South", "East", "West"]
visited_positions = []

# Start a little away from the exit
position = [3, 2]

# Step 1 – Main loop
while True:
    steps += 1

    # Step 2 – Random direction
    direction = random.choice(directions)
    if direction == "North":
        position[1] += 1
    elif direction == "South":
        position[1] -= 1
    elif direction == "East":
        position[0] += 1
    else:  # West
        position[0] -= 1

    visited_positions.append([position[0], position[1]])

    # Step 4 – Status message every 10 steps
    if steps % 10 == 0:
        print(f"Step {steps}: Position ({position[0]}, {position[1]})")

    # Step 3 – Exit found?
    if position == exit_position:
        print(f"🎉 Exit found after {steps} steps!")
        break

    # Step 3 – Give up after 100 steps
    if steps >= 100:
        print(f"😵 Lost in the labyrinth after {steps} steps!")
        break

print(f"Visited {len(visited_positions)} different squares in total.")