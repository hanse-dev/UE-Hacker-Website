# Schritt 1 – Zaubernamen erzeugen
def generiere_zauber_name(element_typ, stufe):
    return f"{element_typ.upper()}-L{stufe}"

# Schritt 2 – Zaubermacht berechnen
def berechne_macht(komplexitaet, element_typ):
    faktoren = {"Feuer": 1.5, "Wasser": 1.0, "Erde": 0.8, "Luft": 1.2}
    faktor = faktoren.get(element_typ, 1.0)
    macht = min(100, int(komplexitaet * faktor * 10))
    return macht

# Schritt 3 – Zauber-Daten erstellen
def erstelle_zauber(element_typ, stufe, komplexitaet):
    name = generiere_zauber_name(element_typ, stufe)
    macht = berechne_macht(komplexitaet, element_typ)
    return {"name": name, "element": element_typ, "stufe": stufe, "macht": macht}

# Schritt 4 – Zauberbuch verwalten
zauberbuch = []

def speichere_zauber(buch, zauber):
    buch.append(zauber)

# Schritt 5 – Generator nutzen
speichere_zauber(zauberbuch, erstelle_zauber("Feuer", 3, 7))
speichere_zauber(zauberbuch, erstelle_zauber("Wasser", 1, 4))
speichere_zauber(zauberbuch, erstelle_zauber("Erde", 2, 5))
speichere_zauber(zauberbuch, erstelle_zauber("Luft", 4, 6))
speichere_zauber(zauberbuch, erstelle_zauber("Feuer", 5, 9))

print("=== ZAUBERBUCH ===")
for z in zauberbuch:
    print(f"{z['name']} – Element: {z['element']}, Stufe: {z['stufe']}, Macht: {z['macht']}")

gesamt_macht = sum(z["macht"] for z in zauberbuch)
durchschnitt = gesamt_macht // len(zauberbuch)
print(f"\nAnzahl Zauber: {len(zauberbuch)}")
print(f"Durchschnittliche Macht: {durchschnitt}")

# Bonus – sortiert nach Macht
print("\n--- Sortiert nach Macht ---")
sortiert = sorted(zauberbuch, key=lambda z: z["macht"], reverse=True)
for z in sortiert:
    print(f"  {z['name']}: {z['macht']}")