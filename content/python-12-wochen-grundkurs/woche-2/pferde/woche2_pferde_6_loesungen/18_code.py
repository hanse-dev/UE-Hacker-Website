# Schritt 1 – Futter erfassen (8 Säcke)
sack1_sorte = "Hafer"
sack1_gewicht = 25.0
sack2_sorte = "Heu"
sack2_gewicht = 40.5
sack3_sorte = "Gerste"
sack3_gewicht = 18.0
sack4_sorte = "Maisschrot"
sack4_gewicht = 32.0
sack5_sorte = "Kleie"
sack5_gewicht = 15.5
sack6_sorte = "Luzerne"
sack6_gewicht = 28.0
sack7_sorte = "Rübenschnitzel"
sack7_gewicht = 22.0
sack8_sorte = "Kraftfutter"
sack8_gewicht = 12.5

# Schritt 2 – Futterprotokoll erstellen
print("=== FUTTERRAUM-PROTOKOLL ===")
print(f"Sack 1 – {sack1_sorte}: {sack1_gewicht} kg")
print(f"Sack 2 – {sack2_sorte}: {sack2_gewicht} kg")
print(f"Sack 3 – {sack3_sorte}: {sack3_gewicht} kg")
print(f"Sack 4 – {sack4_sorte}: {sack4_gewicht} kg")
print(f"Sack 5 – {sack5_sorte}: {sack5_gewicht} kg")
print(f"Sack 6 – {sack6_sorte}: {sack6_gewicht} kg")
print(f"Sack 7 – {sack7_sorte}: {sack7_gewicht} kg")
print(f"Sack 8 – {sack8_sorte}: {sack8_gewicht} kg")
print()

# Schritt 3 – Durchschnitt berechnen
gesamtgewicht = sack1_gewicht + sack2_gewicht + sack3_gewicht + sack4_gewicht + sack5_gewicht + sack6_gewicht + sack7_gewicht + sack8_gewicht
durchschnitt = gesamtgewicht / 8
print(f"Durchschnittsgewicht: {durchschnitt} kg")

# Schritt 4 – Schwerster Sack
print(f"Schwerster Sack: {sack2_sorte} mit {sack2_gewicht} kg")

# Schritt 5 – Gesamtgewicht
print(f"Gesamtgewicht: {gesamtgewicht} kg")

# Bonus
unter_durchschnitt = 0
if sack1_gewicht < durchschnitt: unter_durchschnitt += 1
if sack2_gewicht < durchschnitt: unter_durchschnitt += 1
if sack3_gewicht < durchschnitt: unter_durchschnitt += 1
if sack4_gewicht < durchschnitt: unter_durchschnitt += 1
if sack5_gewicht < durchschnitt: unter_durchschnitt += 1
if sack6_gewicht < durchschnitt: unter_durchschnitt += 1
if sack7_gewicht < durchschnitt: unter_durchschnitt += 1
if sack8_gewicht < durchschnitt: unter_durchschnitt += 1
print(f"Säcke unter Durchschnitt: {unter_durchschnitt}")