# Problem: __init__ needs self as first parameter – otherwise Python doesn't know
# on which object the attributes (name, level) should be stored.
class Rider:
    def __init__(self, name, level):
        self.name = name
        self.level = level

maria = Rider("Maria", 3)
print(maria.name)