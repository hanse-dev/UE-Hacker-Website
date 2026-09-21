class Supply:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Supply(self.amount + other.amount)

    def __eq__(self, other):
        return self.amount == other.amount

print(Supply(10) + Supply(40) == Supply(50))
