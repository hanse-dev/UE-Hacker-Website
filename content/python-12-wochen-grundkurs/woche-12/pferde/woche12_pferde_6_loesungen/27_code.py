class Ausreisser:
    def __init__(self, name, puste, tempo):
        self.name = name
        self.puste = puste
        self.tempo = tempo

    def ist_eingefangen(self):
        return self.puste <= 0

bock = Ausreisser("Ziegenbock", 10, 3)
print(bock.ist_eingefangen())
bock.puste = 0
print(bock.ist_eingefangen())
