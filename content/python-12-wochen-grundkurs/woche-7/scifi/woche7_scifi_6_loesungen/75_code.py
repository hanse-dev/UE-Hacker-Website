import random

werte = []
for i in range(10):
    werte.append(random.randint(60, 140))
alle_ok = True
summe = 0
hoechster = werte[0]
for wert in werte:
    if wert < 60 or wert > 140:
        alle_ok = False
    summe += wert
    if wert > hoechster:
        hoechster = wert
durchschnitt = summe / len(werte)
print(f"Anzahl: {len(werte)}")
print(f"Alle im Bereich: {alle_ok}")
print(f"Höchster mindestens Durchschnitt: {hoechster >= durchschnitt}")
