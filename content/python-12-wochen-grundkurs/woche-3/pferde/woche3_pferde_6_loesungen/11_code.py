# Schritt 1 – Zugangsdaten
alter = 14
hat_helm = True
hat_erlaubnis = False

# Schritt 2 & 3 – Zugangsregel
if alter >= 12 or hat_helm or hat_erlaubnis:
    print("Zugang zum Stall gewährt! Willkommen!")
    # Bonus: Helm-Pflicht unter 16
    if alter < 16 and not hat_helm:
        print("Hinweis: Bitte Helm aufsetzen!")
else:
    print("Zugang verweigert!")
    print("Du brauchst: Alter >= 12, einen Helm oder eine Erlaubnis.")