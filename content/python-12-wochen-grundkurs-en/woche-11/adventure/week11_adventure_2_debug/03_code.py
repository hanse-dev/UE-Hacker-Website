class dragon:
    def fly():
        print("The dragon flies!")

class firebreather(dragon):
    def breathe_fire():
        print("Fire! 🔥")

dragon = firebreather()
dragon.fly()
