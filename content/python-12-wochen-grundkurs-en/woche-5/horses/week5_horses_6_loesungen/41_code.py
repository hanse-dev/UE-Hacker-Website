def has_room(boxes, horses):
    return boxes >= horses

print(f"Barn: {has_room(12, 10)}")
print(f"Pasture: {has_room(5, 8)}")
