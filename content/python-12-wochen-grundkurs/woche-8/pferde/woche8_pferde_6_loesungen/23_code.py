zubehoer = ("Sattel", 15, "Leder")
try:
    zubehoer[1] = 99
except TypeError:
    print("Fehler: geschützt")
