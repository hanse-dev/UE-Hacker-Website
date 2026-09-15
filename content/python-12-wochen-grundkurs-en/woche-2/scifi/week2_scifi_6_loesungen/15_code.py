# Step 1 – Catalogue asteroids
asteroid1_name = "Kepler-99A"
asteroid1_minerals = 5000
asteroid1_purity = 0.85
asteroid1_value_per_kg = 12.0

asteroid2_name = "Vega-17B"
asteroid2_minerals = 3500
asteroid2_purity = 0.97
asteroid2_value_per_kg = 18.5

# Step 2 – Calculate raw value
raw_value1 = asteroid1_minerals * asteroid1_purity * asteroid1_value_per_kg
raw_value2 = asteroid2_minerals * asteroid2_purity * asteroid2_value_per_kg

# Step 3 – Value comparison
print(f"{asteroid1_name}: Raw value {raw_value1} Cyber Credits")
print(f"{asteroid2_name}: Raw value {raw_value2} Cyber Credits")
print()

if raw_value1 > raw_value2:
    more_valuable = asteroid1_name
else:
    more_valuable = asteroid2_name

# Step 4 – Mining decision
print(f"More valuable asteroid: {more_valuable} will be mined!")
average_value = (raw_value1 + raw_value2) / 2
print(f"Average value: {average_value:.2f} Cyber Credits")

# Bonus
value_diff = abs(raw_value1 - raw_value2)
print(f"Value difference: {value_diff:.2f} Cyber Credits")