class Held:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __eq__(self, other):
        return self.level == other.level

a = Held("Aria", 5)
print(a == Held("Thorin", 5))
print(a == Held("Luna", 8))
