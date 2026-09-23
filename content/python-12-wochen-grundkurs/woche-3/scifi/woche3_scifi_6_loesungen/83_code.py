erfolgreiche_phasen = 4
gefahrenstufe = 4
gesamtpunkte = erfolgreiche_phasen * 100 - gefahrenstufe * 20
erfolgsquote = (erfolgreiche_phasen / 5) * 100
print(f"Gesamtpunkte: {gesamtpunkte}, Erfolgsquote: {erfolgsquote}%")
