class Horse:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Horse('{self.name}')"

print([Horse("Blitz"), Horse("Stella")])
