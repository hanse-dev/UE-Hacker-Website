class Held:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Held('{self.name}')"

print([Held("Aria"), Held("Thorin")])
