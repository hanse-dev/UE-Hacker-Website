class price:
    def __init__(value):
        self.value = value

    def __add__(other):
        return self.value + other.value

price1 = price(1000)
price2 = price(2000)
total = price1 + price2
print(f"Total price: {total} euros")
