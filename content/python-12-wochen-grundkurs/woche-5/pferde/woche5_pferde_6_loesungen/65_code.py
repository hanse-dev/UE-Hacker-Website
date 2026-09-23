def berechne_futterkosten(pferde, tage):
    return pferde * tage * 4

def reicht_das_geld(kosten, geld):
    return geld >= kosten
def stallbericht(stall, pferde, tage, geld):
    kosten = berechne_futterkosten(pferde, tage)
    print(f"Stall {stall}")
    print(f"Futterkosten: {kosten}")
    print(f"Reicht: {reicht_das_geld(kosten, geld)}")

stallbericht("Nord", 10, 7, 300)
