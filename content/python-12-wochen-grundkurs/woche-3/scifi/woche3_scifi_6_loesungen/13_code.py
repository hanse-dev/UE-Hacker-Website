# Schritt 1 – Passwörter festlegen
admin_passwort = "Nexus-7-Alpha"
gast_passwort = "GalaxyGuest"

# Schritt 2 – Eingabe simulieren
eingabe = "Nexus-7-Alpha"

# Schritt 3 & 4 – Zugriffsprüfung
if eingabe == admin_passwort:
    print("Admin erkannt! Vollzugriff gewährt!")
    print("Alle Systeme zugänglich: Navigation, Waffen, Kommunikation")
elif eingabe == gast_passwort:
    print("Gast erkannt! Lesezugriff gewährt.")
    print("Nur Navigationsdaten lesbar.")
else:
    print("Falsches Passwort! Zugriff verweigert.")
    # Bonus: Hinweise
    if len(eingabe) < 8:
        print("Tipp: Das Passwort ist länger als 8 Zeichen.")
    else:
        print("Tipp: Sonderzeichen und Großbuchstaben prüfen!")