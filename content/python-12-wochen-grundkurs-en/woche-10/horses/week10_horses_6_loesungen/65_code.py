class Saddle:
    def __init__(self, name, value):
        self.name = name
        self.value = value

lager = [Saddle("Show saddle", 50), Saddle("Riding blanket", 35), Saddle("Halter", 20)]
for g in lager:
    print(f"{g.name}: {g.value}")
