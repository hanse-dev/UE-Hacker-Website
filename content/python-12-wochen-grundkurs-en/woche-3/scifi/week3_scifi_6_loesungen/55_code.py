level = 9
success_points = 90
losses = 1
time = 24
score = success_points - (losses * 10) - (time / 5)
if level >= 10 and score >= 85 and losses == 0:
    print("LEGENDARY!")
elif level >= 8 and score >= 70 and losses <= 2:
    print("EXCELLENT!")
else:
    print("Mission completed.")
