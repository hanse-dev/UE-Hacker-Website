# Problem: __init__ needs self as first parameter – otherwise Python doesn't know
# on which object the attributes (name, power_level) should be stored.
class Cyborg:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

terminator = Cyborg("T-800", 9000)
print(terminator.name)