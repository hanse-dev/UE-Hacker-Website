# Schritt 1: Disziplinen anlegen
turnierplan = {
    "Dressur": {"richter": "Dr. Weber", "uhrzeit": "09:00", "max_teilnehmer": 8, "teilnehmer": []},
    "Springen": {"richter": "Frau Schmidt", "uhrzeit": "11:00", "max_teilnehmer": 6, "teilnehmer": []},
    "Gelaenderitt": {"richter": "Herr Müller", "uhrzeit": "14:00", "max_teilnehmer": 10, "teilnehmer": []}
}

# Schritt 2: Reiter zuordnen
reiter = {"name": "Lena", "level": 3, "pferd": "Thunder"}
turnierplan["Dressur"]["teilnehmer"].append(reiter["name"])
turnierplan["Springen"]["teilnehmer"].append(reiter["name"])

# Schritt 3: Übersicht ausgeben
print("=== TURNIERPLAN ===")
for disziplin, info in turnierplan.items():
    freie_plaetze = info["max_teilnehmer"] - len(info["teilnehmer"])
    status = "Plätze frei" if freie_plaetze > 0 else "Ausgebucht!"
    print(f"\n{disziplin}:")
    print(f"  Richter:         {info['richter']}")
    print(f"  Uhrzeit:         {info['uhrzeit']}")
    print(f"  Teilnehmer:      {info['teilnehmer']}")
    print(f"  Freie Plätze:    {freie_plaetze} – {status}")

# Bonus: Uhrzeiten als Tupel
uhrzeiten = tuple(info["uhrzeit"] for info in turnierplan.values())
print(f"\nBonus – Zeitplan: {uhrzeiten}")