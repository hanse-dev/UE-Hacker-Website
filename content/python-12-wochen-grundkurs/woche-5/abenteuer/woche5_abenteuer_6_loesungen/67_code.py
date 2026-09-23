def berechne_schaden(basis, ruestung):
    schaden = basis - ruestung
    if schaden < 0:
        return 0
    return schaden

print(f"Schaden: {berechne_schaden(40, 15)}")
print(f"Schaden: {berechne_schaden(10, 30)}")
