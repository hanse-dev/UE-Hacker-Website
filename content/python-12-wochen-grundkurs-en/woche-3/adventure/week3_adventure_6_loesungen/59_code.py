level = 50
wins = 20
losses = 0
win_rate = wins / (wins + losses)

if level >= 50 and win_rate > 0.8:
    print("LEGENDARY!")