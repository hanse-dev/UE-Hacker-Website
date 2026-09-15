# Problem: Class names must start with capital letters
class Animal:
    def __init__(self, name):
        self.name = name

class Horse(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

stormy = Horse("Stormy", "Icelandic Horse")
print(stormy.name)
