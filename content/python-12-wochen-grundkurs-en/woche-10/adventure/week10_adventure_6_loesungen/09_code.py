class Hero:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

a = Hero("Luna")
b = Hero("Thorin", 7)
print(f"{a.name}: Level {a.level}")
print(f"{b.name}: Level {b.level}")
