points = 95
errors = 1
time = 80
score = points - (errors * 5) - (time / 10)
if score >= 85 and errors == 0:
    print("🥇 GOLD!")
elif score >= 70 and errors <= 2:
    print("🥈 SILVER!")
