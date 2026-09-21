class Roboter:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Roboter('{self.name}')"

print([Roboter("Nova"), Roboter("Orbit")])
