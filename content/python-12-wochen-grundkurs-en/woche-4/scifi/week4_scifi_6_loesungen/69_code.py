player_row = 1
player_col = 1
target_row = 8
target_col = 8
while player_row < 8:
    player_row += 1
    player_col += 1
if player_row == target_row and player_col == target_col:
    print("🎯 Target reached!")
