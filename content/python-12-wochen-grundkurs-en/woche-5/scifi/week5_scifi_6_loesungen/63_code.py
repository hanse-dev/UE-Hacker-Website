def is_fuel_enough(demand, supply):
    return supply >= demand

print(f"Enough: {is_fuel_enough(280, 300)}")
print(f"Enough: {is_fuel_enough(280, 200)}")
