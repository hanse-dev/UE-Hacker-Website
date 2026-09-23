leben = 100
tiefe = 0
while leben > 0:
    tiefe += 1
    leben -= 15
    if tiefe == 4 or tiefe == 8:
        leben += 20
print(f"Tiefste Tiefe: {tiefe}")
