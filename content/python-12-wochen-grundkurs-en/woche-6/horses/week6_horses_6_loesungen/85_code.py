def create_tournament(name, place, difficulty):
    return [name, place, difficulty]

tournaments = []
tournaments.append(create_tournament("Jumping Show", "Arena", 4))
print(tournaments[0])
