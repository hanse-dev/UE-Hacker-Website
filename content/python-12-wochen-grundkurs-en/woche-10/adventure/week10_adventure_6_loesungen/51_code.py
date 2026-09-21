class Sword:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def info(self):
        return f"{self.name} ({self.value})"

print(Sword("Excalibur", 50).info())
print(Sword("Nightblade", 35).info())
