class Team:
    def __init__(self):
        self.mitglieder = []

    def __len__(self):
        return len(self.mitglieder)

team = Team()
team.mitglieder.append("Nova")
team.mitglieder.append("Orbit")
team.mitglieder.append("Zeta")
print(len(team))
