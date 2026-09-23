class Tool:
    def __init__(self, name, value):
        self.name = name
        self.value = value

lager = [Tool("Plasma laser", 50), Tool("Ion blaster", 35), Tool("Welding torch", 20)]
for g in lager:
    print(f"{g.name}: {g.value}")
