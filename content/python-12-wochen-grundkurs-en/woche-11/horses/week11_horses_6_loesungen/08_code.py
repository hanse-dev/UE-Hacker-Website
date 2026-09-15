# Problem: Class names must start with capital letters
# and __add__ should return a new object
class Price:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Price(self.value + other.value)

    def __str__(self):
        return f"{self.value} euros"

price1 = Price(1000)
price2 = Price(2000)
total = price1 + price2
print(f"Total price: {total}")
