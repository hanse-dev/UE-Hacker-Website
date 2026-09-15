# Beispiel 1: Verschiedene Docstring-Stile
def einfache_funktion():
    """Dies ist ein einzeiliger Docstring."""
    return "Einfach"

def detaillierte_funktion(schiff_name, flotten_id):
    """Erstellt eine Missions-Beschreibung.
    
    Args:
        schiff_name (str): Der Name des Schiffs
        flotten_id (int): Die ID der Flotte
    
    Returns:
        str: Eine formatierte Beschreibung
    """
    return f"{schiff_name} gehört zur Flotte {flotten_id}."

# Docstring aufrufen (so funktioniert es!)
print("=== Docstring-Beispiele ===")
print(f"Einfacher Docstring: {einfache_funktion.__doc__}")
print()
print(f"Detaillierter Docstring: {detaillierte_funktion.__doc__}")