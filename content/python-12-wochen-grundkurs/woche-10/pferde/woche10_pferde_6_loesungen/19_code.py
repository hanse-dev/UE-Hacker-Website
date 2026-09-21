class Pferd:
    def __init__(self, name, energie):
        self.name = name
        self.energie = energie

    def ist_muede(self):
        return self.energie < 20

print(Pferd("Blitz", 10).ist_muede())
print(Pferd("Stella", 80).ist_muede())
