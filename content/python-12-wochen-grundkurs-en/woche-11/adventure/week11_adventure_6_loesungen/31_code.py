class Hero:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Hero('{self.name}')"

print([Hero("Aria"), Hero("Thorin")])
