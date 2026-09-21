spell1_name = "Fireball"
spell1_power = 85.0
spell1_complexity = 3
spell1_duration = 2

spell2_name = "Frostbolt"
spell2_power = 60.0
spell2_complexity = 2
spell2_duration = 1

spell3_name = "Storm"
spell3_power = 95.0
spell3_complexity = 5
spell3_duration = 4

total_complexity = spell1_complexity + spell2_complexity + spell3_complexity
average_power = (spell1_power + spell2_power + spell3_power) / 3
print(f"Total complexity: {total_complexity}, average power: {average_power}")