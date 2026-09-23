position = 0
steps = 0
while position < 50 and steps < 10:
    position += 3
    steps += 1
if position < 50:
    print(f"Lost in the labyrinth after {steps} steps")
