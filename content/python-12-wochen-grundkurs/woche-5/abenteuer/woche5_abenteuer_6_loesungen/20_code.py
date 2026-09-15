# Schritt 1 – Abteilungen erzeugen
def erstelle_abteilung(abteilung_id, groesse):
    return {"id": abteilung_id, "groesse": groesse, "mana": 0}

abteilungen = [
    erstelle_abteilung("A", 10),
    erstelle_abteilung("B", 6),
    erstelle_abteilung("C", 8),
]

# Schritt 2 – Mana verteilen
def verteile_mana(abteilungen, totales_mana):
    gesamt_groesse = sum(a["groesse"] for a in abteilungen)
    for a in abteilungen:
        a["mana"] = int(totales_mana * a["groesse"] / gesamt_groesse)

verteile_mana(abteilungen, 1000)

# Schritt 3 – Magier-Schichten planen
def plane_magier_schichten(anzahl_magier, schichten):
    pro_schicht = anzahl_magier // schichten
    rest = anzahl_magier % schichten
    verteilung = [pro_schicht + (1 if i < rest else 0) for i in range(schichten)]
    return verteilung

schichtplan = plane_magier_schichten(24, 3)

# Schritt 4 – Gildenbericht
def erzeuge_gildenbericht(abteilungen, gesamt_mana, magier_pro_schicht):
    bericht = "=== GILDENBERICHT ===\n"
    for a in abteilungen:
        bericht += f"Abteilung {a['id']}: Größe {a['groesse']}, Mana {a['mana']}\n"
    bericht += f"Gesamt-Mana: {gesamt_mana}\n"
    bericht += f"Magier pro Schicht: {magier_pro_schicht}"
    return bericht

print(erzeuge_gildenbericht(abteilungen, 1000, schichtplan))

# Bonus – Mana-Warnung
def pruefe_mana(abteilung, mindest_mana=100):
    if abteilung["mana"] < mindest_mana:
        return f"WARNUNG: Abteilung {abteilung['id']} hat nur {abteilung['mana']} Mana!"
    return None

for a in abteilungen:
    warnung = pruefe_mana(a, 200)
    if warnung:
        print(warnung)