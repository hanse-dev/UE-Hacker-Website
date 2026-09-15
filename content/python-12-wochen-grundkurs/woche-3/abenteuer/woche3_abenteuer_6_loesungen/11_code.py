# Schritt 1 – Zugangsdaten
alter = 16
gold = 5
hat_pass = True

# Schritt 2 & 3 – Zugangsregel
if alter >= 18 or gold >= 10 or hat_pass:
    print("Durchgang erlaubt! Weiterreisen, Held!")
    # Bonus: Maut nur ohne Pass
    if not hat_pass:
        print("Maut: 1 Gold bitte!")
else:
    print("Durchgang verweigert!")
    print("Komm wieder, wenn du älter, reicher oder mit Pass bist.")