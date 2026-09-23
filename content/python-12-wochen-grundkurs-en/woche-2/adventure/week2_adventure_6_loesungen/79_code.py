quest1_goal = "Dragon Hunt"
quest1_days = 5
quest1_reward = 500
quest1_group = 4
quest1_success = 0.8

quest2_goal = "Forest Escort"
quest2_days = 3
quest2_reward = 300
quest2_group = 2
quest2_success = 0.5

expected1 = quest1_reward * quest1_success
expected2 = quest2_reward * quest2_success
better = expected1 > expected2
print(f"Quest 1 is more profitable: {better}")