# Schritt 1 – Pferde benennen
pferd1 = "Sturm"
pferd2 = "Sonnenschein"
pferd3 = "Blitz"
reitzeit1 = 45
reitzeit2 = 30
reitzeit3 = 60
schwierigkeit1 = "leicht"
schwierigkeit2 = "mittel"
schwierigkeit3 = "fortgeschritten"

# Schritt 2 – Stundenplan ausgeben
print("=== REITSTUNDEN-PLAN ===")
print(f"{pferd1}: {reitzeit1} Minuten, Schwierigkeit: {schwierigkeit1}")
print(f"{pferd2}: {reitzeit2} Minuten, Schwierigkeit: {schwierigkeit2}")
print(f"{pferd3}: {reitzeit3} Minuten, Schwierigkeit: {schwierigkeit3}")
print()

# Schritt 3 – Gesamtzeit
gesamtzeit = reitzeit1 + reitzeit2 + reitzeit3
print(f"Gesamte Reitzeit: {gesamtzeit} Minuten")

# Schritt 4 – Durchschnittszeit
durchschnitt = gesamtzeit / 3
print(f"Durchschnittszeit: {durchschnitt} Minuten")