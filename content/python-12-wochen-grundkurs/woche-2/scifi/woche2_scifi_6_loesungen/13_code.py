# Schritt 1 – Schiffe benennen
schiff1 = "ISS Aeon"
schiff2 = "ISS Nexus"
schiff3 = "ISS Horizon"
crew1 = 240
crew2 = 180
crew3 = 320
speed1 = 7.2
speed2 = 9.1
speed3 = 6.5

# Schritt 2 – Flottenprotokoll
print("=== FLOTTENANALYSE ===")
print(f"{schiff1}: Crew {crew1}, Geschwindigkeit {speed1} Warp")
print(f"{schiff2}: Crew {crew2}, Geschwindigkeit {speed2} Warp")
print(f"{schiff3}: Crew {crew3}, Geschwindigkeit {speed3} Warp")
print()

# Schritt 3 – Gesamtstärke
gesamt_crew = crew1 + crew2 + crew3
print(f"Gesamtcrew: {gesamt_crew} Personen")

# Schritt 4 – Durchschnittsgeschwindigkeit
gesamt_speed = speed1 + speed2 + speed3
durchschnitt_speed = gesamt_speed / 3
print(f"Durchschnittsgeschwindigkeit: {durchschnitt_speed:.2f} Warp")

# Bonus: Durchschnittliche Crewgröße
print(f"Durchschnittliche Crewgröße: {gesamt_crew / 3:.1f} Personen")