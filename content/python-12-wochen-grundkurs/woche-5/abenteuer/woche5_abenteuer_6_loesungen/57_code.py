def berechne_macht(element, stufe):
    if element == "FEUER":
        return stufe * 30
    elif element == "WASSER":
        return stufe * 20
    else:
        return stufe * 15

print(f"FEUER: {berechne_macht('FEUER', 3)}")
print(f"WASSER: {berechne_macht('WASSER', 3)}")
print(f"ERDE: {berechne_macht('ERDE', 3)}")
