def zauber_name(element, stufe):
    return f"{element}-L{stufe}"

def berechne_macht(element, stufe):
    if element == "FEUER":
        return stufe * 30
    elif element == "WASSER":
        return stufe * 20
    else:
        return stufe * 15
def zeige_zauber(element, stufe):
    print(f"{zauber_name(element, stufe)} hat Macht {berechne_macht(element, stufe)}")

for stufe in range(1, 4):
    zeige_zauber("FEUER", stufe)
