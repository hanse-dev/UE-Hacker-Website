level = 12
wins = 5
losses = 5
win_rate = wins / (wins + losses)
if level >= 50 and win_rate > 0.8:
    print("LEGENDARY!")
elif level >= 30 and win_rate > 0.6:
    print("MASTER!")
else:
    print("FIGHTER")
