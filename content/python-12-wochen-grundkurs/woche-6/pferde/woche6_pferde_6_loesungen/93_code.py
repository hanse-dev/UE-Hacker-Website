namen = ["Hafer", "Heu", "Kraftfutter", "Müsli", "Karotten", "Äpfel", "Stroh", "Mash"]
werte = [120, 45, 300, 80, 210, 15, 95, 95]
summe = 0
for wert in werte:
    summe += wert
durchschnitt = summe / len(werte)
hoechster = 0
for i in range(len(werte)):
    if werte[i] > werte[hoechster]:
        hoechster = i
darunter = 0
for wert in werte:
    if wert < durchschnitt:
        darunter += 1
print(f"Gesamt: {summe}")
print(f"Durchschnitt: {durchschnitt}")
print(f"Höchster: {namen[hoechster]} ({werte[hoechster]})")
print(f"Unter dem Durchschnitt: {darunter}")
