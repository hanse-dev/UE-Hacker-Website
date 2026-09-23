def finde_gewinner(wuerfe):
    beste = 0
    for i in range(len(wuerfe)):
        if wuerfe[i] > wuerfe[beste]:
            beste = i
    return beste

print(f"Gewinner: Spieler {finde_gewinner([4, 6, 2]) + 1}")
