def preis_gesamt(preis, anzahl):
    return preis * anzahl

gesamt = preis_gesamt(25, 4)
geld = 150 - gesamt
print(f"Geld übrig: {geld}")
