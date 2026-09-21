class Supply:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Supply(self.amount + other.amount)

    def __str__(self):
        return f"Supply: {self.amount}"

lager = [Supply(10), Supply(20), Supply(30)]
gesamt = Supply(0)
for v in lager:
    gesamt = gesamt + v
print(gesamt)
