# Beispiel 3: Funktion mit mehreren Parametern
def erstelle_pferd_profil(name, rasse, alter):
    """Erstellt ein Pferd-Profil mit Name, Rasse und Alter"""
    print(f"Pferd-Profil:")
    print(f"  Name: {name}")
    print(f"  Rasse: {rasse}")
    print(f"  Alter: {alter} Jahre")
    print(f"  Status: Bereit für das Training!")

# Verschiedene Pferde-Profile erstellen
print("=== Pferd-Profile ===")
erstelle_pferd_profil("Thunder", "Hannoveraner", 8)
print()
erstelle_pferd_profil("Luna", "Isländer", 5)
print()
erstelle_pferd_profil("Storm", "Quarter Horse", 6)