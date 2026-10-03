admin_passwort = "Nova-7"
gast_passwort = "Stern-3"
eingabe = "Nova-7"
if eingabe == admin_passwort:
    print("Vollzugriff gewährt")
elif eingabe == gast_passwort:
    print("Lesezugriff gewährt")
else:
    print("Zugriff verweigert")