class GoldCoin:
    def __init__(value):
        self.value = value
    
    def __add__(other):
        return self.value + other.value

gold1 = GoldCoin(10)
gold2 = GoldCoin(20)
total = gold1 + gold2
print(total)
