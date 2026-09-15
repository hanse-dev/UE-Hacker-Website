# Schritt 1 – Passwörter festlegen
meister_passwort = "DracheKlinge99"
gast_passwort = "Silberpfeil"

# Schritt 2 – Eingabe simulieren
eingabe = "DracheKlinge99"

# Schritt 3 & 4 – Zugriffsprüfung
if eingabe == meister_passwort:
    print("Meister erkannt! Voller Schatz gewährt!")
    print("Du erhältst: 500 Gold + magische Artefakte!")
elif eingabe == gast_passwort:
    print("Gast erkannt! Teilschatz gewährt.")
    print("Du erhältst: 100 Gold.")
else:
    print("Falsches Passwort!")
    # Bonus: Hinweise
    if len(eingabe) < 5:
        print("Tipp: Das Passwort ist länger als 5 Zeichen.")
    else:
        print("Tipp: Vielleicht ein Großbuchstabe vergessen?")