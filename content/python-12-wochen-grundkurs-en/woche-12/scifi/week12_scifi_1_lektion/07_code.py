# Stage 3a: Items are objects – and they lie in the rooms
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

world["airlock"]["items"] = [Item("Keycard", "It opens secured doors.")]
world["corridor"]["items"] = []
world["lab"]["items"] = [Item("Cutter", "A tool that also stops broken robots.")]
world["reactor"]["items"] = [Item("Powerkey", "The red emergency shutdown key of the reactor.")]

first_room = "airlock"
first_item = world[first_room]["items"][0]
print(f"In the {first_room}: {first_item.name} – {first_item.description}")