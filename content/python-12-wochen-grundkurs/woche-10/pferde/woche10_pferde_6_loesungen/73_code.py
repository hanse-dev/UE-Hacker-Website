class Pferd:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.energie = 50

    def ueberhole(self, ziel):
        ziel.energie -= self.level * 5

a = Pferd("Blitz", 4)
b = Pferd("Stella", 2)
sieger = None
while sieger is None:
    a.ueberhole(b)
    if b.energie <= 0:
        sieger = a
        break
    b.ueberhole(a)
    if a.energie <= 0:
        sieger = b
print(f"Sieger: {sieger.name}")
