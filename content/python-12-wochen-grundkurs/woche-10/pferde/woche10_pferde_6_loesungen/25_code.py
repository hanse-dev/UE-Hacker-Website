class Pferd:
    def __init__(self, name):
        self.name = name
        self.siege = 0

    def gewinne(self):
        self.siege += 1

pferd = Pferd("Blitz")
pferd.gewinne()
pferd.gewinne()
pferd.gewinne()
print(f"Siege: {pferd.siege}")
