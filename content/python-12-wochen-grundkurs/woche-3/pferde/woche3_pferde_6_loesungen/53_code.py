punkte = 95
fehler = 1
zeit = 80
note = punkte - (fehler * 5) - (zeit / 10)

if note >= 85 and fehler == 0:
    print("🥇 GOLD!")
elif note >= 70 and fehler <= 2:
    print("🥈 SILBER!")
