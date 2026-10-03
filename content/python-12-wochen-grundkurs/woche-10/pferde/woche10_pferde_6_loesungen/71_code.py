class Pferd:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.energie = 50

    def ueberhole(self, ziel):
        ziel.energie -= self.level * 5

a = Pferd("Blitz", 4)
b = Pferd("Stella", 2)
a.ueberhole(b)
print(f"{b.name}: {b.energie}")
