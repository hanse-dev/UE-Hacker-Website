import random

# Schritt 1 – Schätze erzeugen
def generiere_schatz(material, seltenheit):
    basis_namen = {
        "Gold": ["Münze", "Barren", "Krone"],
        "Kristall": ["Splitter", "Scherbe", "Kern"],
        "Silber": ["Ring", "Kette", "Becher"],
    }
    namen = basis_namen.get(material, ["Schatz"])
    name = random.choice(namen)
    return [f"{material}-{name}-S{seltenheit}", material, seltenheit]

# Schritt 2 – Statistik berechnen
def berechne_schatz_statistik(schatzliste):
    laenge = len(schatzliste)
    seltenheiten = [s[2] for s in schatzliste]
    durchschnitt = sum(seltenheiten) / laenge if laenge > 0 else 0
    return {"anzahl": laenge, "durchschnitt_seltenheit": round(durchschnitt, 1)}

# Schritt 3 – Mehrere Schätze anlegen
schaetze = []
materialien = ["Gold", "Kristall", "Silber"]
for i in range(1, 11):
    mat = materialien[i % 3]
    schaetze.append(generiere_schatz(mat, i))

print("Schatzliste:")
for s in schaetze:
    print(f"  {s[0]}")

# Schritt 4 – Filtern und sortieren
def filtere_schaetze(schatzliste, suchbegriff):
    return [s for s in schatzliste if suchbegriff.lower() in s[0].lower()]

schaetze.sort(key=lambda s: s[0])
gold_schaetze = filtere_schaetze(schaetze, "Gold")

# Schritt 5 – Katalog zusammenbauen
statistik = berechne_schatz_statistik(schaetze)
print(f"\nAnzahl Schätze: {statistik['anzahl']}")
print(f"Durchschnittliche Seltenheit: {statistik['durchschnitt_seltenheit']}")
print(f"Gold-Schätze gefunden: {len(gold_schaetze)}")
