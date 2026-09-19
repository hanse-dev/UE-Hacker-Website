level1_ok = False
level2_ok = True
level3_ok = True
level4_ok = False
level5_ok = True
erfolge = 0
if level1_ok:
    erfolge = erfolge + 1
if level2_ok:
    erfolge = erfolge + 1
if level3_ok:
    erfolge = erfolge + 1
if level4_ok:
    erfolge = erfolge + 1
if level5_ok:
    erfolge = erfolge + 1
print(f"Erfolge: {erfolge} von 5")