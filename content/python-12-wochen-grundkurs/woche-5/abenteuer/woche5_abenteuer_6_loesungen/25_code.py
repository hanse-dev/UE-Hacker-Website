def summe_bis(n):
    summe = 0
    for zahl in range(1, n + 1):
        summe += zahl
    return summe

print(f"Summe: {summe_bis(10)}")
