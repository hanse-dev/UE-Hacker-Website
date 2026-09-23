class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __eq__(self, other):
        return self.level == other.level

a = Hero("Aria", 5)
print(a == Hero("Thorin", 5))
print(a == Hero("Luna", 8))
