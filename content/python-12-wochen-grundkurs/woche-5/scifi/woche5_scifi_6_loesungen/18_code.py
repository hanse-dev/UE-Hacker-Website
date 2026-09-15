# Schritt 1 – Protokoll-Namen erstellen
def generiere_protokoll_name(system_typ, sicherheits_level):
    return f"{system_typ.upper()}-L{sicherheits_level}"

# Schritt 2 – Effizienz berechnen
def berechne_effizienz(komplexitaet, system_typ):
    faktoren = {"Alarm": 1.5, "Scan": 1.2, "Log": 0.9, "Backup": 1.0}
    faktor = faktoren.get(system_typ, 1.0)
    return min(100, int(komplexitaet * faktor * 8))

# Schritt 3 – Protokoll-Daten erstellen
def erstelle_protokoll(system_typ, sicherheits_level, komplexitaet):
    name = generiere_protokoll_name(system_typ, sicherheits_level)
    effizienz = berechne_effizienz(komplexitaet, system_typ)
    return {"name": name, "typ": system_typ, "level": sicherheits_level, "effizienz": effizienz}

# Schritt 4 – Protokolle speichern
protokolle = []

def speichere_protokoll(liste, protokoll):
    liste.append(protokoll)

# Schritt 5 – Generator-System aufbauen
speichere_protokoll(protokolle, erstelle_protokoll("Alarm", 3, 7))
speichere_protokoll(protokolle, erstelle_protokoll("Scan", 1, 4))
speichere_protokoll(protokolle, erstelle_protokoll("Log", 2, 5))
speichere_protokoll(protokolle, erstelle_protokoll("Backup", 4, 6))
speichere_protokoll(protokolle, erstelle_protokoll("Alarm", 5, 9))

print("=== PROTOKOLL-DATENBANK ===")
for p in protokolle:
    print(f"{p['name']} – Typ: {p['typ']}, Level: {p['level']}, Effizienz: {p['effizienz']}%")

gesamt = sum(p["effizienz"] for p in protokolle)
print(f"\nAnzahl Protokolle: {len(protokolle)}")
print(f"Durchschnittliche Effizienz: {gesamt // len(protokolle)}%")

# Bonus – sortiert nach Effizienz
print("\n--- Sortiert nach Effizienz ---")
for p in sorted(protokolle, key=lambda x: x["effizienz"], reverse=True):
    print(f"  {p['name']}: {p['effizienz']}%")