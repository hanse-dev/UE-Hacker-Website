class Team:
    def __init__(self):
        self.mitglieder = []

    def __len__(self):
        return len(self.mitglieder)

team = Team()
team.mitglieder.append("Aria")
team.mitglieder.append("Thorin")
team.mitglieder.append("Luna")
print(len(team))
