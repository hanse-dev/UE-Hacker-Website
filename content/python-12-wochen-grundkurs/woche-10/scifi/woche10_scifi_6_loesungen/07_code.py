class Roboter:
    def __init__(self, name, level=1, energie=100):
        self.name = name
        self.level = level
        self.energie = energie

roboter = Roboter("Nova", 4)
print(f"{roboter.name} {roboter.level} {roboter.energie}")
