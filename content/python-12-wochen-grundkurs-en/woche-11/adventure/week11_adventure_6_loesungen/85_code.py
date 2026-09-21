class Supply:
    def __init__(self, amount):
        self.amount = amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __str__(self):
        return f"Supply: {self.amount}"

for v in sorted([Supply(30), Supply(10), Supply(20)]):
    print(v)
