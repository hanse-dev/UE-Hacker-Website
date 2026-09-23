def zaehle_spruenge(runden):
    summe = 0
    for runde in range(1, runden + 1):
        summe += runde
    return summe

print(f"Sprünge: {zaehle_spruenge(10)}")
