class Robot:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def win(self):
        self.wins += 1

robot = Robot("Nova")
robot.win()
robot.win()
robot.win()
print(f"Wins: {robot.wins}")
