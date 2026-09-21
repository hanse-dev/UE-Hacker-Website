names = ["Oats", "Hay", "Concentrate", "Muesli", "Carrots", "Apples", "Straw", "Mash"]
values = [120, 45, 300, 80, 210, 15, 95, 95]
total = 0
for value in values:
    total += value
average = total / len(values)
highest = 0
for i in range(len(values)):
    if values[i] > values[highest]:
        highest = i
below = 0
for value in values:
    if value < average:
        below += 1
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Highest: {names[highest]} ({values[highest]})")
print(f"Below average: {below}")
