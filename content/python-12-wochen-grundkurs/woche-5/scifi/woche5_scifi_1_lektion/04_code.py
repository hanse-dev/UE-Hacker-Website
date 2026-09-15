# Mit vs. ohne Klammern
def system_begruessung():
    """Begrüßt Besucher auf der Raumstation"""
    print("Willkommen an Bord der Nebula-7!")

# MIT Klammern: Funktion wird ausgeführt
print("=== Mit Klammern system_begruessung() ===")
system_begruessung()

# OHNE Klammern: Nur Referenz, nichts passiert
print("\n=== Ohne Klammern system_begruessung ===")
print("Typ:", type(system_begruessung))
print("(Die Funktion wurde nicht ausgeführt!)")