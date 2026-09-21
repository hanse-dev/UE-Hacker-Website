class Robot:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Robot('{self.name}')"

print([Robot("Nova"), Robot("Orbit")])
