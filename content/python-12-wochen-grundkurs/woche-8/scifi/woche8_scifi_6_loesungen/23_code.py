bauteil = ("Schildmodul", 15, "Energie")
try:
    bauteil[1] = 99
except TypeError:
    print("Fehler: geschützt")
