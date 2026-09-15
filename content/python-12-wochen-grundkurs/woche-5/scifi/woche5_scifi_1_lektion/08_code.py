# Beispiel 3: Funktion mit mehreren Parametern
def erstelle_schiff_profil(name, klasse, besatzung):
    """Erstellt ein Schiff-Profil mit Name, Klasse und Besatzung"""
    print(f"Schiff-Profil:")
    print(f"  Name: {name}")
    print(f"  Klasse: {klasse}")
    print(f"  Besatzung: {besatzung} Personen")
    print(f"  Status: Bereit für den Einsatz!")

# Verschiedene Schiff-Profile erstellen
print("=== Schiff-Profile ===")
erstelle_schiff_profil("Nebula-Explorer", "Forschungsschiff", 150)
print()
erstelle_schiff_profil("Star-Fighter", "Jäger", 2)
print()
erstelle_schiff_profil("Cargo-Hauler", "Frachter", 25)