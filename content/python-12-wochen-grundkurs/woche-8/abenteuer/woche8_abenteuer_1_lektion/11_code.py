# Beispiel 2: Artefakte sind unveränderlich
zauber_status = ("Aktiv", "Stabil", "Mächtig")
print(f"Zauber-Status: {zauber_status}")

# Zugriff funktioniert
print(f"Status: {zauber_status[0]}")

# Ändern funktioniert NICHT!
try:
    zauber_status[0] = "Inaktiv"
except TypeError as e:
    print(f"Fehler: {e}")

# Aber Artefakte in Listen können geändert werden
zauber = [
    ("Feuerball", "Aktiv"),
    ("Heilung", "Stabil"),
    ("Schild", "Mächtig")
]
zauber[1] = ("Heilung", "Inaktiv")
print(f"\nZauber nach Änderung: {zauber}")