level = 9
verluste = 1
note = 80.0
if level >= 10 and note >= 85 and verluste == 0:
    print("LEGENDÄR!")
elif level >= 8 and note >= 70 and verluste <= 2:
    print("EXZELLENT!")
else:
    print("Mission bestanden.")