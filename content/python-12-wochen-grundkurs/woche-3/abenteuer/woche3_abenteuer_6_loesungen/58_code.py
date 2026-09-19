level = 35
siegquote = 0.9

if level >= 50 and siegquote > 0.8:
    print("LEGENDÄR!")
elif level >= 30 and siegquote > 0.6:
    print("MEISTER!")
else:
    print("KÄMPFER")
