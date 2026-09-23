def ist_trainierbar(fitness, dauer):
    return fitness >= dauer * 2

print(f"Sturmwind: {ist_trainierbar(90, 40)}")
print(f"Blitz: {ist_trainierbar(60, 40)}")
