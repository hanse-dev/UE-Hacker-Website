class Gegner:
    def __init__(self, name, hp, staerke):
        self.name = name
        self.hp = hp
        self.staerke = staerke

    def ist_besiegt(self):
        return self.hp <= 0

feind = Gegner("Wartungsroboter", 10, 3)
print(feind.ist_besiegt())
feind.hp = 0
print(feind.ist_besiegt())
