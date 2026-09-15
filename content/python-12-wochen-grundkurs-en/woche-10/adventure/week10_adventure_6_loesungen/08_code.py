# Problem: Methods always need self as first parameter – without self the method
# cannot access self.name (it doesn't know which dragon is meant).
class Dragon:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"I am {self.name}!")

dragon = Dragon("Smaug")
dragon.introduce()