# Mit vs. ohne Klammern
def begruessung_reiterhof():
    """Begrüßt Besucher auf dem Reiterhof"""
    print("Willkommen auf dem Reiterhof Sonnental!")

# MIT Klammern: Funktion wird ausgeführt
print("=== Mit Klammern begruessung_reiterhof() ===")
begruessung_reiterhof()

# OHNE Klammern: Nur Referenz, nichts passiert
print("\n=== Ohne Klammern begruessung_reiterhof ===")
print("Typ:", type(begruessung_reiterhof))
print("(Die Funktion wurde nicht ausgeführt!)")