# Problem: Class names must start with capital letters
# and methods need self as the first parameter
class Horse:
    def neigh(self):
        print("Neigh! 🐴")

class Arab(Horse):
    def gallop(self):
        print("Fast as the wind!")

my_horse = Arab()
my_horse.neigh()
