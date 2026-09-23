def zaehle_signale(sektoren):
    summe = 0
    for sektor in range(1, sektoren + 1):
        summe += sektor
    return summe

print(f"Signale: {zaehle_signale(10)}")
