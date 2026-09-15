# Schritt 1 – Sektoren erzeugen
def erstelle_sektor(sektor_id, groesse):
    return {"id": sektor_id, "groesse": groesse, "energie": 0}

sektoren = [
    erstelle_sektor("Alpha", 5),
    erstelle_sektor("Beta", 3),
    erstelle_sektor("Gamma", 7),
]

# Schritt 2 – Energie verteilen
def verteile_energie(sektoren, gesamt_energie):
    gesamt_groesse = sum(s["groesse"] for s in sektoren)
    for s in sektoren:
        s["energie"] = round(gesamt_energie * s["groesse"] / gesamt_groesse, 1)

verteile_energie(sektoren, 1500)

# Schritt 3 – Schichtplanung
def plane_schichten(anzahl_personal, schichten):
    pro_schicht = anzahl_personal // schichten
    rest = anzahl_personal % schichten
    return [pro_schicht + (1 if i < rest else 0) for i in range(schichten)]

schichtplan = plane_schichten(15, 3)

# Schritt 4 – Stations-Übersicht erzeugen
def erzeuge_stationsbericht(sektoren, energie_gesamt, personal):
    bericht = "=== STATIONSBERICHT NEBULA-7 ===\n"
    for s in sektoren:
        bericht += f"  Sektor {s['id']}: Größe {s['groesse']}, Energie {s['energie']} EE\n"
    bericht += f"Gesamt-Energie: {energie_gesamt} EE\n"
    bericht += f"Personal pro Schicht: {personal}"
    return bericht

print(erzeuge_stationsbericht(sektoren, 1500, schichtplan))

# Bonus – Energie-Warnung
def energie_notfall(sektor, mindest_energie=100):
    if sektor["energie"] < mindest_energie:
        return f"NOTFALL: Sektor {sektor['id']} – nur {sektor['energie']} EE verfügbar!"
    return None

for s in sektoren:
    warnung = energie_notfall(s)
    if warnung:
        print(warnung)