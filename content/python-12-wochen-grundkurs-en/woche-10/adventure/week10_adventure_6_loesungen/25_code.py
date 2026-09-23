class Hero:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def win(self):
        self.wins += 1

hero = Hero("Aria")
hero.win()
hero.win()
hero.win()
print(f"Wins: {hero.wins}")
