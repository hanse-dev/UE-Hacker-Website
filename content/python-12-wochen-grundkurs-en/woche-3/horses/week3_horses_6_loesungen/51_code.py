points = 95
errors = 0
time = 55
score = points - (errors * 5) - (time / 10)
if score >= 85 and errors == 0:
    print("🥇 GOLD!")
