reward1 = 500
duration1 = 4
group1 = 5
chance1 = 0.8
reward2 = 800
duration2 = 7
group2 = 4
chance2 = 0.75
expected1 = reward1 * chance1
expected2 = reward2 * chance2
print(f"Quest 2 more profitable: {expected2 > expected1}")
