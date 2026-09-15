import random

# Step 1 – Tournament plan
def create_participant(name, discipline, start_points):
    return {"name": name, "discipline": discipline, "points": start_points}

# Step 2 – Calculate points
def calculate_points(scores, difficulty):
    average = sum(scores) / len(scores)
    return round(average * difficulty, 1)

# Step 3 – Check requirements
def can_participate(rider_level, min_level, has_equipment):
    return rider_level >= min_level and has_equipment

# Step 4 – Tournament result
def show_tournament_result(participants):
    print("=== TOURNAMENT RESULTS ===")
    sorted_list = sorted(participants, key=lambda t: t["points"], reverse=True)
    for i, p in enumerate(sorted_list, 1):
        print(f"  {i}. {p['name']} ({p['discipline']}): {p['points']} points")
    print(f"\nWinner: {sorted_list[0]['name']} with {sorted_list[0]['points']} points!")

participants = [
    create_participant("Lena", "Dressage", 0),
    create_participant("Max", "Jumping", 0),
    create_participant("Sophie", "Dressage", 0),
]

for p in participants:
    scores = [random.randint(6, 10) for _ in range(3)]
    difficulty = random.uniform(1.0, 1.5)
    p["points"] = calculate_points(scores, difficulty)

show_tournament_result(participants)

# Bonus – ranking
print("\n--- Ranking ---")
for i, p in enumerate(sorted(participants, key=lambda x: x["points"], reverse=True), 1):
    print(f"  Place {i}: {p['name']} – {p['points']} pts")