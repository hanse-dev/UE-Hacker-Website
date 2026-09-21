class Held:
    def __init__(self, name):
        self.name = name
        self.siege = 0

    def gewinne(self):
        self.siege += 1

held = Held("Aria")
held.gewinne()
held.gewinne()
held.gewinne()
print(f"Siege: {held.siege}")
