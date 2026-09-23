def calculate_feed_costs(horses, days):
    return horses * days * 4

def is_money_enough(costs, money):
    return money >= costs
def barn_report(barn, horses, days, money):
    costs = calculate_feed_costs(horses, days)
    print(f"Barn {barn}")
    print(f"Feed costs: {costs}")
    print(f"Enough: {is_money_enough(costs, money)}")

barn_report("North", 10, 7, 300)
