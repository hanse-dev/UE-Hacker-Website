class Roboter:
    def __init__(self, name, energie):
        self.name = name
        self.energie = energie

    def ist_muede(self):
        return self.energie < 20

print(Roboter("Nova", 10).ist_muede())
print(Roboter("Orbit", 80).ist_muede())
