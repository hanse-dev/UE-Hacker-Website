danger_level = 4
successful_phases = 2

if danger_level >= 4:
    if successful_phases < 3:
        print("Rescue required!")
    else:
        print("Hold the line")
else:
    print("All quiet")