def kosten_gesamt(preis, anzahl):
    return preis * anzahl

gesamt = kosten_gesamt(15, 4)
gold = 100 - gesamt
print(f"Gold übrig: {gold}")
