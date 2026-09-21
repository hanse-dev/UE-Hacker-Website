def berechne_kosten(magier, tage):
    return magier * tage * 5

def ist_bezahlbar(kosten, gold):
    return gold >= kosten
def gildenbericht(abteilung, magier, tage, gold):
    kosten = berechne_kosten(magier, tage)
    print(f"Abteilung {abteilung}")
    print(f"Kosten: {kosten}")
    print(f"Bezahlbar: {ist_bezahlbar(kosten, gold)}")

gildenbericht("Feuer", 6, 5, 200)
