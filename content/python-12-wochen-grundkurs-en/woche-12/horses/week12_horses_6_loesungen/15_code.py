class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

x = Item("Flashlight", "It lights up dark corners.")
print(x.name)
