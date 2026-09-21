def calculate_fuel(ships, days):
    return ships * days * 4

def is_fuel_enough(demand, supply):
    return supply >= demand
def fleet_report(fleet, ships, days, supply):
    demand = calculate_fuel(ships, days)
    print(f"Fleet {fleet}")
    print(f"Fuel: {demand}")
    print(f"Enough: {is_fuel_enough(demand, supply)}")

fleet_report("Alpha", 10, 7, 300)
