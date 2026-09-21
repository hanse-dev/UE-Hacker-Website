def calculate_profit(jobs, failures):
    return jobs * 10 - failures * 5

print(f"Profit: {calculate_profit(8, 2)}")
