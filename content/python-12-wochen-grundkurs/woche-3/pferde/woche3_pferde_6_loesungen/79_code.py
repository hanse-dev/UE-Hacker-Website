level1_ok = True
level2_ok = True
level3_ok = False
level4_ok = False
level5_ok = True

erfolge = 0
if level1_ok:
    erfolge += 1
if level2_ok:
    erfolge += 1
if level3_ok:
    erfolge += 1
if level4_ok:
    erfolge += 1
if level5_ok:
    erfolge += 1
print(f"Erfolge: {erfolge} von 5")
