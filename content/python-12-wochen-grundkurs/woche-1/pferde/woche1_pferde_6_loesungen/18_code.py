# Schritt 1 – Futtergedicht verfassen
zeile1 = "Gutes Futter macht das Pferd gesund und stark"
zeile2 = "Frisches Heu duftet durch den ganzen Stall"
zeile3 = "Karotten bringen Freude, Hafer gibt die Kraft"
zeile4 = "So pflegt man seinen Vierbeiner mit viel Bedacht"

# Schritt 2 – Bucheintrag
titel = "Das Lied vom guten Futter"
verfasser = "Lena vom Sonnenhof"
karotten_bewertung = 5

# Schritt 3 – Gedicht formatiert ausgeben
print("=== " + titel + " ===")
print("---")
print(zeile1)
print(zeile2)
print(zeile3)
print(zeile4)
print()

# Schritt 4 – Metadaten
print("Verfasser: " + verfasser)
print("Bewertung: " + str(karotten_bewertung) + " Karotten")

# Bonus: geheimes Futterrezept als Kommentar
# Geheimrezept: 3 Karotten + 1 Apfel + Prise Salz = magische Energie für 24h