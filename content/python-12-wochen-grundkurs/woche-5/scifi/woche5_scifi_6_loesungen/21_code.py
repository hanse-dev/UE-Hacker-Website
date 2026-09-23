def preis_gesamt(preis, anzahl):
    return preis * anzahl

gesamt = preis_gesamt(30, 3)
credits = 100 - gesamt
print(f"Credits übrig: {credits}")
