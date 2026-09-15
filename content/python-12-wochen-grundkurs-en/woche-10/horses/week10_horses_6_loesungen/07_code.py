# Problem: Methods always need self as first parameter – without self the method
# cannot access self.name (it doesn't know which horse is meant).
class Horse:
    def __init__(self, name):
        self.name = name
    
    def gallop(self):
        print(f"{self.name} is galloping! 🐎")

horse = Horse("Spirit")
horse.gallop()