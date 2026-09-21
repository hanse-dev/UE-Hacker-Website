class Team:
    def __init__(self):
        self.mitglieder = []

    def __len__(self):
        return len(self.mitglieder)

team = Team()
team.mitglieder.append("Blitz")
team.mitglieder.append("Stella")
team.mitglieder.append("Sturm")
print(len(team))
