# Beispiel 2: Tupel sind unveränderlich
system_status = ("Online", "Stabil", "Aktiv")
print(f"System-Status: {system_status}")

# Zugriff funktioniert
print(f"Status: {system_status[0]}")

# Ändern funktioniert NICHT!
try:
    system_status[0] = "Offline"
except TypeError as e:
    print(f"Fehler: {e}")

# Aber Tupel in Listen können geändert werden
systeme = [
    ("Navigation", "Online"),
    ("Antrieb", "Stabil"),
    ("Kommunikation", "Aktiv")
]
systeme[1] = ("Antrieb", "Offline")
print(f"\nSysteme nach Änderung: {systeme}")