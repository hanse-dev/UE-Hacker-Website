world = {
    "yard": {
        "description": "You stand in the yard. The moon is shining, and you hear a soft whinny from the stable.",
        "exits": {"north": "aisle"},
    },
    "aisle": {
        "description": "A long stable aisle. The horses' stalls are on both sides.",
        "exits": {"south": "yard", "east": "paddock", "west": "saddlery"},
    },
    "saddlery": {"description": "The saddlery smells of leather. Saddles and bridles hang on the wall.", "exits": {"east": "aisle"}},
    "paddock": {"description": "The paddock at night. The foal stands in the grass – and in front of it an angry goat!", "exits": {"west": "aisle"}},
}

def describe(room_name):
    room = world[room_name]
    print(f"📍 {room_name.capitalize()}: {room['description']}")
    print("   Exits:", ", ".join(room["exits"]))

def go(position, direction):
    exits = world[position]["exits"]
    if direction in exits:
        new_position = exits[direction]
        describe(new_position)
        return new_position
    print("🚫 You can't go that way!")
    return position

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

world["yard"]["items"] = [Item("Flashlight", "It lights up dark corners.")]
world["aisle"]["items"] = []
world["saddlery"]["items"] = [Item("Broom", "A sturdy broom. It helps to chase away the goat.")]
world["paddock"]["items"] = [Item("Foal", "The little foal follows you trustfully.")]

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.hp = 20
        self.inventory = []

    def go(self, direction):
        exits = world[self.position]["exits"]
        if direction in exits:
            self.position = exits[direction]
            describe(self.position)
            self.look_around()
        else:
            print("🚫 You can't go that way!")

    def look_around(self):
        items = world[self.position]["items"]
        if items:
            names = [g.name for g in items]
            print("👀 You see:", ", ".join(names))
        else:
            print("👀 Nothing lies here.")

    def take(self, item_name):
        room = world[self.position]
        for item in room["items"]:
            if item.name == item_name:
                room["items"].remove(item)
                self.inventory.append(item)
                print(f"🎒 You take: {item.name} – {item.description}")
                return
        print(f"❓ There is no '{item_name}' here.")

    def show_inventory(self):
        if self.inventory:
            names = [g.name for g in self.inventory]
            print("🎒 In the bag:", ", ".join(names))
        else:
            print("🎒 Your bag is empty.")

player = Player("Mira", "yard")
player.take("Flashlight")
def has_item(player, name):
    for item in player.inventory:
        if item.name == name:
            return True
    return False

print(has_item(player, "Flashlight"))
print(has_item(player, "Broom"))
