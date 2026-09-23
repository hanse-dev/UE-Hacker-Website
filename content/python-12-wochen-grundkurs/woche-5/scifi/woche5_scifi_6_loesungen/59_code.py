def berechne_schildbonus(module):
    if module >= 5:
        return 20
    elif module >= 3:
        return 10
    else:
        return 0

def berechne_schild(energie, module):
    return energie * 3 + berechne_schildbonus(module)
def zeige_schild(name, energie, module):
    print(f"{name}: Schild {berechne_schild(energie, module)}")

for module in range(2, 7, 2):
    zeige_schild("Nova", 30, module)
