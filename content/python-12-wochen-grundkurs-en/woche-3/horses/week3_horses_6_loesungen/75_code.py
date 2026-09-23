level1_ok = True
level2_ok = True
level3_ok = False
level4_ok = False
level5_ok = True
successes = 0
if level1_ok:
    successes += 1
if level2_ok:
    successes += 1
if level3_ok:
    successes += 1
if level4_ok:
    successes += 1
if level5_ok:
    successes += 1
print(f"Successes: {successes} of 5")
