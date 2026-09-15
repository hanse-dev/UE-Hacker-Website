# Problem: __add__ should return a new object
class GoldCoin:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return GoldCoin(self.value + other.value)
    
    def __str__(self):
        return f"{self.value} Gold Coins"

gold1 = GoldCoin(10)
gold2 = GoldCoin(20)
total = gold1 + gold2
print(total)
