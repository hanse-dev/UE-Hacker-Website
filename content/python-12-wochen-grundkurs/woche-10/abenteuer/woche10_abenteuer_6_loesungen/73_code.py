class Held:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.energie = 50

    def greife_an(self, ziel):
        ziel.energie -= self.level * 5

a = Held("Aria", 4)
b = Held("Thorin", 2)
sieger = None
while sieger is None:
    a.greife_an(b)
    if b.energie <= 0:
        sieger = a
        break
    b.greife_an(a)
    if a.energie <= 0:
        sieger = b
print(f"Sieger: {sieger.name}")
