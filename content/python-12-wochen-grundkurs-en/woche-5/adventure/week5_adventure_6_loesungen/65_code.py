def calculate_costs(mages, days):
    return mages * days * 5

def is_affordable(costs, gold):
    return gold >= costs
def guild_report(department, mages, days, gold):
    costs = calculate_costs(mages, days)
    print(f"Department {department}")
    print(f"Costs: {costs}")
    print(f"Affordable: {is_affordable(costs, gold)}")

guild_report("Fire", 6, 5, 200)
