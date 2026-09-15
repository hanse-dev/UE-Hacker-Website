# Schritt 1 – Schiffsdaten erstellen
schiffstyp = "Kreuzer"
registrierung = "NCC-2048"
baujahr = 2387

# Schritt 2 – Daten strukturiert ausgeben
print("=== SCHIFFSPROTOKOLL ===")
print("Schiffstyp: " + schiffstyp)
print("Registrierung: " + registrierung)
print("Baujahr: " + str(baujahr))

# Schritt 3 – Vollständiger Bericht
print()
print(schiffstyp + " " + registrierung + ", Baujahr " + str(baujahr) + ", ist einsatzbereit.")
print("=== ENDE PROTOKOLL ===")