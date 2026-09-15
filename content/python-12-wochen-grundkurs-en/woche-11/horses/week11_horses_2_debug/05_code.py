class animal:
    def __init__(name):
        self.name = name

class horse(animal):
    def __init__(name, breed):
        super().__init__(name)
        self.breed = breed

stormy = horse("Stormy", "Icelandic Horse")
print(stormy.name)
