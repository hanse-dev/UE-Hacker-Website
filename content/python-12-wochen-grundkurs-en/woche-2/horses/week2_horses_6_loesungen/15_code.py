# Step 1 – Record horses
horse1_name = "Thundercloud"
horse1_age = 8
horse1_dressage = 88
horse1_jumping = 92

horse2_name = "Silver Wind"
horse2_age = 6
horse2_dressage = 95
horse2_jumping = 79

# Step 2 – Calculate total points
total1 = horse1_dressage + horse1_jumping
total2 = horse2_dressage + horse2_jumping

# Step 3 – Determine winner
print(f"{horse1_name} (Age {horse1_age}): {total1} points")
print(f"{horse2_name} (Age {horse2_age}): {total2} points")
print()

if total1 > total2:
    winner = horse1_name
else:
    winner = horse2_name

# Step 4 – Victory announcement
print(f"The tournament winner is: {winner}!")
average_points = (total1 + total2) / 2
print(f"Average points: {average_points}")

# Bonus
lead = abs(total1 - total2)
print(f"Winner's lead: {lead} points")