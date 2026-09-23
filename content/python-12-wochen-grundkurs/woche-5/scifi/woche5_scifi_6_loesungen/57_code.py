def berechne_schildbonus(module):
    if module >= 5:
        return 20
    elif module >= 3:
        return 10
    else:
        return 0
def berechne_schild(energie, module):
    return energie * 3 + berechne_schildbonus(module)

print(f"Schild: {berechne_schild(30, 6)}")
