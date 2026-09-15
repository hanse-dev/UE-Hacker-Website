# Beispiel 1: Verschiedene Docstring-Stile
def einfache_funktion():
    """Dies ist ein einzeiliger Docstring."""
    return "Einfach"

def detaillierte_funktion(pferd_name, training_level):
    """Erstellt eine Trainings-Beschreibung.
    
    Args:
        pferd_name (str): Der Name des Pferdes
        training_level (int): Das Trainings-Level des Pferdes
    
    Returns:
        str: Eine formatierte Beschreibung
    """
    return f"{pferd_name} hat Trainings-Level {training_level}."

# Docstring aufrufen (so funktioniert es!)
print("=== Docstring-Beispiele ===")
print(f"Einfacher Docstring: {einfache_funktion.__doc__}")
print()
print(f"Detaillierter Docstring: {detaillierte_funktion.__doc__}")