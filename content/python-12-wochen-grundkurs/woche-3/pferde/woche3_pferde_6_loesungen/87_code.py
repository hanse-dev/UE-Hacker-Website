erfolgreiche_phasen = 4
schwierigkeit = 4

gesamtpunkte = erfolgreiche_phasen * 100 - schwierigkeit * 20
quote = (erfolgreiche_phasen / 5) * 100
print(f"Gesamtpunkte: {gesamtpunkte}, Erfolgsquote: {quote}%")
