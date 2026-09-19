level1_ok = True
level2_ok = True
level3_ok = False
level4_ok = True
level5_ok = True
successes = 0
if level1_ok:
    successes = successes + 1
if level2_ok:
    successes = successes + 1
if level3_ok:
    successes = successes + 1
if level4_ok:
    successes = successes + 1
if level5_ok:
    successes = successes + 1
print(f"Levels passed: {successes} of 5")