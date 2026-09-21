scores = {"Mira": 120, "Tom": 90, "Lena": 150}
beste = None
for name in scores:
    if beste is None or scores[name] > scores[beste]:
        beste = name
print(f"Best: {beste}")
