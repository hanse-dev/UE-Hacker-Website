# Schritt 1 – Passwörter festlegen
stallmeister_passwort = "GoldenerHuf2024"
pfleger_passwort = "Strohballen"

# Schritt 2 – Eingabe simulieren
eingabe = "GoldenerHuf2024"

# Schritt 3 & 4 – Zugriffsprüfung
if eingabe == stallmeister_passwort:
    print("Stallmeister erkannt! Vollzugriff gewährt!")
    print("Alle Futtervorräte verfügbar: Heu, Hafer, Karotten, Äpfel")
elif eingabe == pfleger_passwort:
    print("Pfleger erkannt! Futterzugriff gewährt.")
    print("Verfügbar: Heu und Hafer")
else:
    print("Falsches Passwort!")
    # Bonus: Hinweise
    if len(eingabe) < 6:
        print("Tipp: Das Passwort ist länger als 6 Zeichen.")
    else:
        print("Tipp: Groß- und Kleinschreibung beachten!")