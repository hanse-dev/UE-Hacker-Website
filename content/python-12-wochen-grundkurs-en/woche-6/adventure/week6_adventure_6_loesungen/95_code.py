strengths = [80, 55, 95, 40, 70]
total = 0
for s in strengths:
    total += s
average = total / len(strengths)
above = [s for s in strengths if s > average]
print(f"Average: {average}")
print(above)
