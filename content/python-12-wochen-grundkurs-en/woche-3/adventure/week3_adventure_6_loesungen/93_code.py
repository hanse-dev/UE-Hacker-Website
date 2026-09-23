danger_level = 5
successful_phases = 2
if danger_level >= 4:
    if successful_phases < 3:
        print("Rescue required!")
    else:
        print("The squad holds out.")
else:
    print("No danger for the squad.")
