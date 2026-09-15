# Mit vs. ohne Klammern
def gruesse_abenteurer():
    """Begrüßt einen tapferen Abenteurer"""
    print("Willkommen, tapferer Held!")

# MIT Klammern: Funktion wird ausgeführt
print("=== Mit Klammern gruesse_abenteurer() ===")
gruesse_abenteurer()

# OHNE Klammern: Nur Referenz, nichts passiert
print("\n=== Ohne Klammern gruesse_abenteurer ===")
print("Typ:", type(gruesse_abenteurer))
print("(Die Funktion wurde nicht ausgeführt!)")