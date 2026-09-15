import random

# Schritt 1 – Charakter-Grunddaten
def erstelle_charakter(name, klasse, level):
    """Erstellt ein Charakter-Dictionary.
    
    Parameter:
        name (str): Name des Charakters
        klasse (str): Klasse des Charakters (z.B. 'Magier', 'Krieger')
        level (int): Aktuelles Level des Charakters
    
    Ergebnis:
        dict: Dictionary mit name, klasse und level
    """
    return {"name": name, "klasse": klasse, "level": level}

# Schritt 2 – Lebenspunkte berechnen
def berechne_leben(level, klasse):
    basis = {"Magier": 50, "Schurke": 70, "Krieger": 100, "Heiler": 80}
    basis_leben = basis.get(klasse, 75)
    return basis_leben + level * 10

# Schritt 3 – Ausrüstung erstellen
def generiere_ausruestung(klasse):
    sets = {
        "Magier": ["Magierstab", "Zaubermantel", "Zauberbuch"],
        "Krieger": ["Langschwert", "Kettenrüstung", "Rundschild"],
        "Schurke": ["Dolch", "Lederrüstung", "Wurfmesser"],
        "Heiler": ["Heilstab", "Gewand", "Kräutertasche"]
    }
    return sets.get(klasse, ["Holzstab", "Lumpengewand"])

# Schritt 4 – Charakterbogen anzeigen
def zeige_charakterbogen(charakter, leben, ausruestung):
    print("=" * 30)
    print("      CHARAKTERBOGEN")
    print("=" * 30)
    print(f"Name:    {charakter['name']}")
    print(f"Klasse:  {charakter['klasse']}")
    print(f"Level:   {charakter['level']}")
    print(f"Leben:   {leben} LP")
    print("Ausrüstung:")
    for item in ausruestung:
        print(f"  - {item}")
    print("=" * 30)

# Alles zusammen
held = erstelle_charakter("Aldric", "Krieger", 7)
leben = berechne_leben(held["level"], held["klasse"])
ausruestung = generiere_ausruestung(held["klasse"])
zeige_charakterbogen(held, leben, ausruestung)

# Bonus – zufällige Stats
held["staerke"] = random.randint(10, 30)
held["intelligenz"] = random.randint(5, 20)
print(f"Stärke: {held['staerke']} | Intelligenz: {held['intelligenz']}")