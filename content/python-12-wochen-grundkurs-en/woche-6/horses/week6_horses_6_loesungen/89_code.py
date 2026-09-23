tournaments = [["Jumping Show", "Arena", 4], ["Dressage Show", "Ring", 2], ["Trail Ride", "Forest", 3]]
def tournament_statistics(items):
    count = 0
    hard = 0
    for tournament in items:
        count += 1
        if tournament[2] < 3:
            continue
        hard += 1
    print(f"Tournaments: {count}")
    print(f"Hard tournaments: {hard}")

tournament_statistics(tournaments)
