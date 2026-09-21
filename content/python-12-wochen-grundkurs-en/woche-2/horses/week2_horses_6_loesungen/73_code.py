cost1 = 250.0
people1 = 10
cost2 = 180.0
people2 = 8
per1 = cost1 / people1
per2 = cost2 / people2
unit2_cheaper = per2 < per1
print(f"Unit 2 is cheaper per participant: {unit2_cheaper}")