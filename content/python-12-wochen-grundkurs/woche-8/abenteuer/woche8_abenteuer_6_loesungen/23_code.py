artefakt = ("Feuerstab", 15, "Feuer")
try:
    artefakt[1] = 99
except TypeError:
    print("Fehler: geschützt")
