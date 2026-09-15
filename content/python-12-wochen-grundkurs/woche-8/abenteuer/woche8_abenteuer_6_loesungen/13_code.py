# Schritt 1: Artefakte als Tupel
artefakt1 = ("Feuerschwert", 30, "Feuer")
artefakt2 = ("Eisring", 12, "Eis")
print(f"Artefakt 1: {artefakt1} | Länge: {len(artefakt1)}")
print(f"Artefakt 2: {artefakt2} | Länge: {len(artefakt2)}")

# Schritt 2: Tupel-Unpacking
name1, staerke1, element1 = artefakt1
print(f"\nUnpacking Artefakt 1: Name={name1}, Stärke={staerke1}, Element={element1}")

name2, staerke2, element2 = artefakt2
print(f"Unpacking Artefakt 2: Name={name2}, Stärke={staerke2}, Element={element2}")

# Schritt 3: Artefakt-Dictionary
artefakte = {
    "Feuerstab": ("Stab", 15, "Feuer"),
    "Eisring": ("Ring", 5, "Eis"),
    "Blitzaxt": ("Axt", 25, "Blitz")
}
print(f"\nArtefakt-Dictionary: {artefakte}")
print(f"Feuerstab: {artefakte['Feuerstab']}")

# Schritt 4: Vergleich der Stärken
differenz = abs(staerke1 - staerke2)
print(f"\nStärke-Differenz zwischen {name1} und {name2}: {differenz}")

# Bonus: 4D-Artefakt
artefakt_4d = ("Zeitstab", 50, "Zeit", 3)  # Name, Stärke, Element, Dimensionen
a_name, a_st, a_el, a_dim = artefakt_4d
print(f"\nBonus 4D-Artefakt: {a_name} | {a_dim} Dimensionen")