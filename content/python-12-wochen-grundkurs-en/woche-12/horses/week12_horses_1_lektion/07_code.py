# Stage 3a: Items are objects – and they lie in the rooms
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

world["yard"]["items"] = [Item("Flashlight", "It shines in dark corners.")]
world["aisle"]["items"] = []
world["tackroom"]["items"] = [Item("Broom", "A sturdy broom. It helps to chase off the billy goat.")]
world["paddock"]["items"] = [Item("Foal", "The little foal follows you trustingly.")]

first_room = "yard"
first_item = world[first_room]["items"][0]
print(f"In the {first_room}: {first_item.name} – {first_item.description}")