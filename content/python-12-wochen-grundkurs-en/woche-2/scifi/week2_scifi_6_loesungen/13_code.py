# Step 1 – Name the ships
ship1 = "ISS Aeon"
ship2 = "ISS Nexus"
ship3 = "ISS Horizon"
crew1 = 240
crew2 = 180
crew3 = 320
speed1 = 7.2
speed2 = 9.1
speed3 = 6.5

# Step 2 – Fleet protocol
print("=== FLEET ANALYSIS ===")
print(f"{ship1}: Crew {crew1}, Speed {speed1} warp")
print(f"{ship2}: Crew {crew2}, Speed {speed2} warp")
print(f"{ship3}: Crew {crew3}, Speed {speed3} warp")
print()

# Step 3 – Total strength
total_crew = crew1 + crew2 + crew3
print(f"Total crew: {total_crew} people")

# Step 4 – Average speed
total_speed = speed1 + speed2 + speed3
average_speed = total_speed / 3
print(f"Average speed: {average_speed:.2f} warp")

# Bonus: average crew size
print(f"Average crew size: {total_crew / 3:.1f} people")