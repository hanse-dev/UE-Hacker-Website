level = 35
wins = 18
losses = 6
win_rate = wins / (wins + losses)

if level >= 50 and win_rate > 0.8:
    print("LEGENDARY!")
elif level >= 30 and win_rate > 0.6:
    print("MASTER!")
else:
    print("Fighter")