health = 100
mana = 50
depth = 0
while health > 0 and mana > 0:
    health -= 15
    mana -= 10
    depth += 1
print(f"Depth {depth}, health {health}, mana {mana}")
