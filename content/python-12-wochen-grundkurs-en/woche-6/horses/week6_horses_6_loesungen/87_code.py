tournaments = [["Jumping Show", "Arena", 4], ["Dressage Show", "Ring", 2], ["Trail Ride", "Forest", 3]]
def search_tournaments(items, term):
    found = []
    for tournament in items:
        if term in tournament[0]:
            found.append(tournament)
    return found

hits = search_tournaments(tournaments, "Show")
print(f"Found: {len(hits)}")
