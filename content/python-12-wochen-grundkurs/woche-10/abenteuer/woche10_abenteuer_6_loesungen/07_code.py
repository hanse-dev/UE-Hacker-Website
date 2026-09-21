class Held:
    def __init__(self, name, level=1, energie=100):
        self.name = name
        self.level = level
        self.energie = energie

held = Held("Aria", 4)
print(f"{held.name} {held.level} {held.energie}")
