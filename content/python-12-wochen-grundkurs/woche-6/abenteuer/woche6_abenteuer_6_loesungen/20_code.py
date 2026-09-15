import random

# Schritt 1 – Tresorfächer anlegen
def erstelle_tresorfaecher(anzahl_faecher, plaetze_pro_fach):
    return [["leer"] * plaetze_pro_fach for _ in range(anzahl_faecher)]

faecher = erstelle_tresorfaecher(3, 4)

# Schritt 2 – Schätze einlagern
def platziere_schatz(faecher, fach_index, schatz_name):
    for i, platz in enumerate(faecher[fach_index]):
        if platz == "leer":
            faecher[fach_index][i] = schatz_name
            return True
    return False

platziere_schatz(faecher, 0, "Goldbarren")
platziere_schatz(faecher, 0, "Kristallkern")
platziere_schatz(faecher, 1, "Silberkrone")
platziere_schatz(faecher, 2, "Rubinring")
platziere_schatz(faecher, 2, "Saphirkette")

# Schritt 3 – Bewachung verteilen
def verteile_bewachung(faecher, gesamte_bewachung):
    belegungen = [len([s for s in f if s != "leer"]) for f in faecher]
    gesamt = sum(belegungen) or len(faecher)
    return [round(gesamte_bewachung * (b / gesamt), 1) if gesamt > 0 else gesamte_bewachung / len(faecher) for b in belegungen]

bewachung_liste = verteile_bewachung(faecher, 300)

# Schritt 4 – Übersicht ausgeben
def zeige_uebersicht(faecher):
    gesamt_plaetze = sum(len(f) for f in faecher)
    print(f"=== TRESOR-ÜBERSICHT ===")
    for i, fach in enumerate(faecher):
        schaetze = [s for s in fach if s != "leer"]
        print(f"  Fach {i+1}: {schaetze if schaetze else 'leer'}")
    print(f"Fächer: {len(faecher)} | Gesamtplätze: {gesamt_plaetze}")

zeige_uebersicht(faecher)
print(f"Bewachungs-Verteilung: {bewachung_liste}")

# Bonus – zufällige Einbruchsversuche und Prüfung
einbruchsversuche = [80, 150, 250]
versuch = random.choice(einbruchsversuche)
print(f"\nEinbruchsversuch mit Stärke: {versuch}")
fach_index = 0
ausreichend_bewacht = bewachung_liste[fach_index] >= versuch
print(f"Fach {fach_index+1} hält stand: {ausreichend_bewacht}")
