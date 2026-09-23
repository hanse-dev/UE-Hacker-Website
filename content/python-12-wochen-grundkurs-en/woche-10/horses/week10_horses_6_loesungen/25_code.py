class Horse:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def win(self):
        self.wins += 1

horse = Horse("Blitz")
horse.win()
horse.win()
horse.win()
print(f"Wins: {horse.wins}")
