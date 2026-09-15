import random

# Schritt 1 – Missions-Profil erstellen
def erstelle_missions_profil(name, ziel, prioritaet):
    """Erstellt ein Missionsprofil.
    
    Parameter:
        name (str): Name der Mission
        ziel (str): Zielkoordinaten oder Zielbeschreibung
        prioritaet (int): Prioritätsstufe (1 = niedrig, 5 = höchste)
    
    Ergebnis:
        dict: Dictionary mit name, ziel, prioritaet
    """
    return {"name": name, "ziel": ziel, "prioritaet": prioritaet}

# Schritt 2 – Reisezeit berechnen
def berechne_reisezeit(distanz, geschwindigkeit):
    return distanz / geschwindigkeit

# Schritt 3 – Missionsbericht erstellen
def generiere_bericht(profil, reisezeit):
    bericht = f"=== MISSIONSBERICHT ===\n"
    bericht += f"Name:      {profil['name']}\n"
    bericht += f"Ziel:      {profil['ziel']}\n"
    bericht += f"Priorität: {profil['prioritaet']}/5\n"
    bericht += f"Reisezeit: {reisezeit:.1f} Stunden\n"
    bericht += "=" * 22
    return bericht

# Schritt 4 – Planungs-System
profil = erstelle_missions_profil("Omega-Scan", "Sektor Delta-9", 4)
reisezeit = berechne_reisezeit(450, 30)
bericht = generiere_bericht(profil, reisezeit)
print(bericht)

# Bonus – Raumwetter und Hindernisse
def zufalls_raumwetter():
    wetter = random.choice(["ruhig", "Meteorsturm", "Sonnenwind"])
    hindernis = random.choice(["keins", "Asteroidenfeld", "Raumpiraten"])
    return wetter, hindernis

wetter, hindernis = zufalls_raumwetter()
print(f"Raumwetter: {wetter} | Hindernis: {hindernis}")