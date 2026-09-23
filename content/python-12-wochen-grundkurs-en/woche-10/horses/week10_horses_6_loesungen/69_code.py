class Saddle:
    def __init__(self, name, value):
        self.name = name
        self.value = value

lager = [Saddle("Show saddle", 50), Saddle("Riding blanket", 35), Saddle("Halter", 20)]
summe = 0
for g in lager:
    summe += g.value
print(f"Sum: {summe}")
