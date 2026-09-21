def berechne_schildbonus(module):
    if module >= 5:
        return 20
    elif module >= 3:
        return 10
    else:
        return 0

print(f"Bonus: {berechne_schildbonus(6)}")
print(f"Bonus: {berechne_schildbonus(4)}")
print(f"Bonus: {berechne_schildbonus(1)}")
