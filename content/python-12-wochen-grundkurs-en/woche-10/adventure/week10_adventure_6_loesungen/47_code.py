class Sword:
    def __init__(self, name, value):
        self.name = name
        self.value = value

sword = Sword("Excalibur", 50)
print(f"{sword.name}: {sword.value}")
