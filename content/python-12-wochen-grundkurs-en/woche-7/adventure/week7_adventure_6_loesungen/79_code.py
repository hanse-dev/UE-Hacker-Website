import random

position = 0
path = [0]
steps = 0
while steps < 100:
    position += random.choice([-1, 1])
    path.append(position)
    steps += 1
    if position == 5:
        break
print(f"At most 100 steps: {steps <= 100}")
print(f"Path fits: {len(path) == steps + 1}")
