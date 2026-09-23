scores = {"Mira": 120, "Tom": 90, "Lena": 150}
for name in sorted(scores, key=scores.get, reverse=True):
    print(f"{name}: {scores[name]}")
