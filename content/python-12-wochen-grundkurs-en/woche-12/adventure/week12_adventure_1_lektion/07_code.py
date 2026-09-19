# Stage 3a: Items are objects – and they lie in the rooms
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

world["entrance"]["items"] = [Item("Torch", "It shines in dark corners.")]
world["hall"]["items"] = []
world["spring"]["items"] = [Item("Sword", "A sharp sword stuck in the stone next to the spring.")]
world["treasury"]["items"] = [Item("Treasure", "The legendary treasure of Pyralia!")]

first_room = "entrance"
first_item = world[first_room]["items"][0]
print(f"In the {first_room}: {first_item.name} – {first_item.description}")