menge = 0
while menge < 2:
    menge = int(input())
    if menge < 2:
        print("Zu wenig Heu!")
print(f"Fütterung: {menge} kg")
