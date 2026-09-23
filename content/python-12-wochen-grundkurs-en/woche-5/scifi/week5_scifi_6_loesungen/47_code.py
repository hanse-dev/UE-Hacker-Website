def calculate_profit(jobs, failures):
    return jobs * 10 - failures * 5

def create_id(name, number):
    return f"{number}: {name}"
def show_mission_report(name, number, jobs, failures):
    print(create_id(name, number))
    print(f"Profit: {calculate_profit(jobs, failures)}")
    print(f"Failures: {failures}")

show_mission_report("Nova", 7, 8, 2)
