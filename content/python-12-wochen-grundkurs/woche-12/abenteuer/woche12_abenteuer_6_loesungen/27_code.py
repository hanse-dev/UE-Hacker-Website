class Gegner:
    def __init__(self, name, hp, staerke):
        self.name = name
        self.hp = hp
        self.staerke = staerke

    def ist_besiegt(self):
        return self.hp <= 0

foe = Gegner("Drache", 10, 3)
print(foe.ist_besiegt())
foe.hp = 0
print(foe.ist_besiegt())
