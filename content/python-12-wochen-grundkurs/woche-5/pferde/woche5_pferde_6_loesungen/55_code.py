def berechne_zeitbonus(sekunden):
    if sekunden <= 60:
        return 20
    elif sekunden <= 90:
        return 10
    else:
        return 0

print(f"Bonus: {berechne_zeitbonus(55)}")
print(f"Bonus: {berechne_zeitbonus(80)}")
print(f"Bonus: {berechne_zeitbonus(100)}")
