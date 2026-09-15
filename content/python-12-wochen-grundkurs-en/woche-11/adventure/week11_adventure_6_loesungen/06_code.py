# Problem: No error – super() is used correctly!
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Bello", "Dachshund")
print(dog.name)
