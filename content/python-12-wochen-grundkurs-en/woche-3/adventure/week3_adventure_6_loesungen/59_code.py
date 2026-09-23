level = 35
win_rate = 0.9
if level >= 50 and win_rate > 0.8:
    print("LEGENDARY!")
elif level >= 30 and win_rate > 0.6:
    print("MASTER!")
else:
    print("FIGHTER")
