class Saddle:
    def __init__(self, name, value):
        self.name = name
        self.value = value

lager = [Saddle("Show saddle", 50), Saddle("Riding blanket", 35), Saddle("Halter", 20)]
beste = lager[0]
for g in lager:
    if g.value > beste.value:
        beste = g
print(f"Strongest: {beste.name}")
