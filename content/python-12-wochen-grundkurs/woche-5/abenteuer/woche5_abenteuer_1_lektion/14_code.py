# Beispiel 1: Verschiedene Docstring-Stile
def einfache_funktion():
    """Dies ist ein einzeiliger Docstring."""
    return "Einfach"

def detaillierte_funktion(name, level):
    """Erstellt eine Charakter-Beschreibung.
    
    Args:
        name (str): Der Name des Charakters
        level (int): Das Level des Charakters
    
    Returns:
        str: Eine formatierte Beschreibung
    """
    return f"{name} ist ein Level {level} Charakter."

# Docstring aufrufen (so funktioniert es!)
print("=== Docstring-Beispiele ===")
print(f"Einfacher Docstring: {einfache_funktion.__doc__}")
print()
print(f"Detaillierter Docstring: {detaillierte_funktion.__doc__}")