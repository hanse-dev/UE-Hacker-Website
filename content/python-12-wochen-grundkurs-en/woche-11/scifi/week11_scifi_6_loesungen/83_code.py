class Team:
    def __init__(self):
        self.mitglieder = []

    def __len__(self):
        return len(self.mitglieder)

    def __str__(self):
        return f"Team: {len(self)}"

t = Team()
t.mitglieder.append("Nova")
t.mitglieder.append("Orbit")
print(t)
