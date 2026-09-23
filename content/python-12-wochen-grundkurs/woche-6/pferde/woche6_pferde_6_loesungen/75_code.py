def berechne_durchschnitt(werte):
    summe = 0
    for wert in werte:
        summe += wert
    return summe / len(werte)

print(f"Durchschnitt: {berechne_durchschnitt([10, 20, 30, 40])}")
