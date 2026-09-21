level = 12
siege = 5
niederlagen = 5
siegquote = siege / (siege + niederlagen)
if level >= 50 and siegquote > 0.8:
    print("LEGENDÄR!")
elif level >= 30 and siegquote > 0.6:
    print("MEISTER!")
else:
    print("KÄMPFER")
