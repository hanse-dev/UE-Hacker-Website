def is_energy_ok(demand, supply):
    return supply >= demand

print(f"Drive: {is_energy_ok(30, 50)}")
print(f"Weapons: {is_energy_ok(40, 25)}")
