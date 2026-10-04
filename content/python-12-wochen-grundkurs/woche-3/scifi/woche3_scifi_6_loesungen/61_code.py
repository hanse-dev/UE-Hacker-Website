frage1 = True
frage2 = True
frage3 = False
frage4 = True
frage5 = False
punkte = 0
if frage1:
    punkte = punkte + 100
if frage2:
    punkte = punkte + 100
if frage3:
    punkte = punkte + 100
if frage4:
    punkte = punkte + 100
if frage5:
    punkte = punkte + 100
if punkte >= 400:
    note = "A"
elif punkte >= 300:
    note = "B"
else:
    note = "C"
print(f"Punkte: {punkte}, Note: {note}")