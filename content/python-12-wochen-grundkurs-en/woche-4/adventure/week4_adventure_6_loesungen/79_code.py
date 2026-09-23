health = 100
depth = 0
while health > 0:
    depth += 1
    health -= 15
    if depth == 4 or depth == 8:
        health += 20
print(f"Deepest depth: {depth}")
