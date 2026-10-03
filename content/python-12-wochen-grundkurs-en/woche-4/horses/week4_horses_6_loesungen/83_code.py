amount = 0
while amount < 2:
    amount = int(input())
    if amount < 2:
        print("Not enough hay!")
print(f"Feeding: {amount} kg")
