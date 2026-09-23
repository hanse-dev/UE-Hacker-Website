class Held:
    def __init__(self, name, energie):
        self.name = name
        self.energie = energie

    def ist_muede(self):
        return self.energie < 20

print(Held("Aria", 10).ist_muede())
print(Held("Thorin", 80).ist_muede())
