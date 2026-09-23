class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

x = Item("Torch", "It lights up dark corners.")
print(x.name)
