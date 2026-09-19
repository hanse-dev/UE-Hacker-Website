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

average_power = (spell1_power + spell2_power + spell3_power) / 3

strong1 = spell1_power > average_power
strong2 = spell2_power > average_power
strong3 = spell3_power > average_power
print(f"{spell1_name} above average: {strong1}")
print(f"{spell2_name} above average: {strong2}")
print(f"{spell3_name} above average: {strong3}")