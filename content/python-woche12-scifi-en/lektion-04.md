# 🚀 Stage 4: Player and Inventory

*Knowledge from week 10: classes*

The **player** remembers where they are, how many hit points they have and what is in the bag. `go()` from stage 2 becomes a **method**.

### 💡 New: objects inside objects (composition)

An object can **contain other objects**: the player has an inventory – a list full of `Item` objects. This is called **composition** ("has a"). Inheritance (week 11), in contrast, says "is a".

```python
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
```

`self.inventory = []` is in `__init__` so that **every** player gets their own bag.
