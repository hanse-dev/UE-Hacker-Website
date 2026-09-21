class Pferd:
    def __init__(self, name, level=1, energie=100):
        self.name = name
        self.level = level
        self.energie = energie

pferd = Pferd("Blitz", 4)
print(f"{pferd.name} {pferd.level} {pferd.energie}")
