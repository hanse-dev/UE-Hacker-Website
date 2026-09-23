class Supply:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Supply(self.amount + other.amount)

    def __str__(self):
        return f"Supply: {self.amount}"

print(Supply(10) + Supply(20))
