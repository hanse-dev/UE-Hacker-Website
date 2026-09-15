# Schritt 1 – Boxen erzeugen
def erstelle_box(box_id, groesse):
    return {"id": box_id, "groesse": groesse, "futter": 0}

boxen = [
    erstelle_box("Box-1", 3),
    erstelle_box("Box-2", 2),
    erstelle_box("Box-3", 4),
]

# Schritt 2 – Futter verteilen
def verteile_futter(boxen, totales_futter):
    gesamt_groesse = sum(b["groesse"] for b in boxen)
    for b in boxen:
        b["futter"] = round(totales_futter * b["groesse"] / gesamt_groesse, 1)

verteile_futter(boxen, 90)

# Schritt 3 – Schichtplanung
def plane_stall_schichten(anzahl_reiter, schichten):
    pro_schicht = anzahl_reiter // schichten
    rest = anzahl_reiter % schichten
    return [pro_schicht + (1 if i < rest else 0) for i in range(schichten)]

schichten = plane_stall_schichten(10, 2)

# Schritt 4 – Stall-Übersicht erzeugen
def erzeuge_stallbericht(boxen, futter_gesamt, reiter_pro_schicht):
    bericht = "=== STALLBERICHT ===\n"
    for b in boxen:
        bericht += f"  {b['id']}: Größe {b['groesse']}, Futter {b['futter']} kg\n"
    bericht += f"Gesamt-Futter: {futter_gesamt} kg\n"
    bericht += f"Reiter pro Schicht: {reiter_pro_schicht}"
    return bericht

print(erzeuge_stallbericht(boxen, 90, schichten))

# Bonus – Futter-Warnung
def pruefe_futter(box, mindest_futter=15):
    if box["futter"] < mindest_futter:
        return f"WARNUNG: {box['id']} hat nur {box['futter']} kg Futter!"
    return None

for b in boxen:
    warnung = pruefe_futter(b)
    if warnung:
        print(warnung)