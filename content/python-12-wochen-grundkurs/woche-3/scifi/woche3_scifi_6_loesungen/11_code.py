# Schritt 1 – Zugangsdaten
rang = 4
hat_ausweis = True
notfall = False

# Schritt 2 & 3 – Zugangsregel
if rang >= 5 or hat_ausweis or notfall:
    print("Zugang zur Brücke gewährt! Scanner bestätigt.")
    # Bonus: Ausweis-Pflicht bei niedrigem Rang
    if rang < 8 and not hat_ausweis:
        print("Hinweis: Ausweis für Rang unter 8 erforderlich!")
else:
    print("Zugang verweigert!")
    print("Fehlende Berechtigung. Scanner-ID ungültig.")