class Sword:
    def __init__(self, name, value):
        self.name = name
        self.value = value

lager = [Sword("Excalibur", 50), Sword("Nightblade", 35), Sword("Iron dagger", 20)]
beste = lager[0]
for g in lager:
    if g.value > beste.value:
        beste = g
print(f"Strongest: {beste.name}")
