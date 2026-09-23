class Sword:
    def __init__(self, name, value):
        self.name = name
        self.value = value

lager = [Sword("Excalibur", 50), Sword("Nightblade", 35), Sword("Iron dagger", 20)]
for g in lager:
    print(f"{g.name}: {g.value}")
