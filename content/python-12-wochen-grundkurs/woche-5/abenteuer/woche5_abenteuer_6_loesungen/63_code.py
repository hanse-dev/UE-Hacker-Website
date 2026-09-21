def ist_bezahlbar(kosten, gold):
    return gold >= kosten

print(f"Bezahlbar: {ist_bezahlbar(150, 200)}")
print(f"Bezahlbar: {ist_bezahlbar(150, 100)}")
