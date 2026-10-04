punkte = 95
fehler = 0
zeit = 55
note = punkte - (fehler * 5) - (zeit / 10)

if note >= 85 and fehler == 0:
    print("🥇 GOLD!")
