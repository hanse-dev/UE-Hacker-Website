level = 9
losses = 1
score = 80.0
if level >= 10 and score >= 85 and losses == 0:
    print("LEGENDARY!")
elif level >= 8 and score >= 70 and losses <= 2:
    print("EXCELLENT!")
else:
    print("Mission completed.")
