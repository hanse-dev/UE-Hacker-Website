kosten1 = 1500
crew1 = 12
chance1 = 0.5
kosten2 = 3000
crew2 = 20
chance2 = 0.75

erfolg1 = kosten1 * chance1
erfolg2 = kosten2 * chance2
titan_besser = erfolg2 > erfolg1
print(f"Gesamtkosten: {kosten1 + kosten2}")
print(f"Gesamtcrew: {crew1 + crew2}")
print(f"Erwarteter Erfolg Mars: {erfolg1}")
print(f"Erwarteter Erfolg Titan: {erfolg2}")
print(f"Titan profitabler: {titan_besser}")