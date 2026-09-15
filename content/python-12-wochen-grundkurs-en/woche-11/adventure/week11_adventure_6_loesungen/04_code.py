# Problem: Class names must start with a capital letter
class Dragon:
    def fly(self):
        print("The dragon flies!")

class Firebreather(Dragon):
    def breathe_fire(self):
        print("Fire! 🔥")

dragon = Firebreather()
dragon.fly()
