class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

x = Item("Keycard", "It opens secured doors.")
print(x.name)
