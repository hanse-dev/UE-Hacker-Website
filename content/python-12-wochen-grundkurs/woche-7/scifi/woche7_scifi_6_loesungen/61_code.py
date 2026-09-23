import random

def finde_gewinner(wuerfe):
    beste = 0
    for i in range(len(wuerfe)):
        if wuerfe[i] > wuerfe[beste]:
            beste = i
    return beste
siege = [0, 0, 0]
for runde in range(5):
    wuerfe = []
    for spieler in range(3):
        wuerfe.append(random.randint(1, 6))
    siege[finde_gewinner(wuerfe)] += 1
gesamt = 0
for s in siege:
    gesamt += s
print(f"Siege insgesamt: {gesamt}")
