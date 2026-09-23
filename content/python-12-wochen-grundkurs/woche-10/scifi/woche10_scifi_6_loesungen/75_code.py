class Roboter:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.energie = 50

    def greife_an(self, ziel):
        ziel.energie -= self.level * 5

a = Roboter("Nova", 4)
b = Roboter("Orbit", 2)
runden = 0
while a.energie > 0 and b.energie > 0:
    runden += 1
    a.greife_an(b)
    if b.energie > 0:
        b.greife_an(a)
print(f"Runden: {runden}")
