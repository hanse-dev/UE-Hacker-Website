# Beispiel 3: Funktion mit mehreren Parametern
def erstelle_charakter(name, klasse, level):
    """Erstellt einen Charakter mit Name, Klasse und Level"""
    print(f"Charakter erstellt:")
    print(f"  Name: {name}")
    print(f"  Klasse: {klasse}")
    print(f"  Level: {level}")
    print(f"  Status: Bereit für Abenteuer!")

# Verschiedene Charaktere erstellen
print("=== Charakter-Erstellung ===")
erstelle_charakter("Aria", "Magierin", 5)
print()
erstelle_charakter("Thorin", "Krieger", 8)
print()
erstelle_charakter("Luna", "Schurkin", 3)