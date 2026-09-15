import random

def initialise_tournament(participant1, participant2):
    return {
        "p1": {"name": participant1["name"], "horse": participant1["horse"], "points": 0},
        "p2": {"name": participant2["name"], "horse": participant2["horse"], "points": 0},
        "discipline": 0
    }

def execute_discipline(rider, horse):
    base = random.randint(60, 100)
    errors = random.randint(0, 3)
    return base, errors

def calculate_points(base_points, error_count):
    deduction = error_count * 5
    return max(0, base_points - deduction)

def start_tournament(participant_a, participant_b, max_disciplines):
    status = initialise_tournament(participant_a, participant_b)
    print(f"=== TOURNAMENT: {participant_a['name']} vs. {participant_b['name']} ===")
    for i in range(1, max_disciplines + 1):
        status["discipline"] = i
        b1, e1 = execute_discipline(status["p1"]["name"], status["p1"]["horse"])
        b2, e2 = execute_discipline(status["p2"]["name"], status["p2"]["horse"])
        p1 = calculate_points(b1, e1)
        p2 = calculate_points(b2, e2)
        status["p1"]["points"] += p1
        status["p2"]["points"] += p2
        print(f"  Discipline {i}: {status['p1']['name']} {p1} pts | {status['p2']['name']} {p2} pts")
    print()
    if status["p1"]["points"] >= status["p2"]["points"]:
        print(f"Winner: {participant_a['name']} ({status['p1']['points']} pts)")
        print(f"Runner-up: {participant_b['name']} ({status['p2']['points']} pts)")
    else:
        print(f"Winner: {participant_b['name']} ({status['p2']['points']} pts)")
        print(f"Runner-up: {participant_a['name']} ({status['p1']['points']} pts)")

rider_a = {"name": "Lena", "horse": "Storm"}
rider_b = {"name": "Max", "horse": "Luna"}
start_tournament(rider_a, rider_b, 3)