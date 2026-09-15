# Step 1 – Fighter data
level = 48
wins = 42
losses = 8

# Step 2 – Calculate win rate
total_fights = wins + losses
win_rate = wins / total_fights
print(f"Fighter: Level {level}, Wins: {wins}, Losses: {losses}")
print(f"Win rate: {win_rate:.0%}")

# Step 3 – Legendary status
if level >= 50 and win_rate > 0.8:
    print("🏆 LEGENDARY! You are a legend of the arena!")
elif level >= 30 and win_rate > 0.6:
    print("⭐ MASTER! A respectable fighter!")
elif level >= 10:
    print("🗡️ WARRIOR – Keep training!")
else:
    print("🌱 APPRENTICE – The path is still long.")

# Step 5 – Perfect streak bonus
if losses == 0:
    print("+100 Bonus for perfect streak!")