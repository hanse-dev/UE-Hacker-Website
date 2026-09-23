class Pferd:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Pferd('{self.name}')"

print([Pferd("Blitz"), Pferd("Stella")])
