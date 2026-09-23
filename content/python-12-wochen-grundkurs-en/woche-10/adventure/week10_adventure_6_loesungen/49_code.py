class Sword:
    def __init__(self, name, value):
        self.name = name
        self.value = value

a = Sword("Excalibur", 50)
b = Sword("Nightblade", 35)
print(f"Together: {a.value + b.value}")
