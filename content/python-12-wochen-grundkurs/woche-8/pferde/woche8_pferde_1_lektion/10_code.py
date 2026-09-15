# Beispiel 3: Kapsel unpacking und Methoden
pferd_daten = ("Thunder", "Hannoveraner", 8, 1.72)

# Kapsel unpacking
name, rasse, alter, groesse = pferd_daten
print("=== Kapsel Unpacking ===")
print(f"Name: {name}")
print(f"Rasse: {rasse}")
print(f"Alter: {alter}")
print(f"Größe: {groesse} m")

# Kapsel-Methoden
print(f"\nAnzahl Elemente: {len(pferd_daten)}")
print(f"Index von 'Hannoveraner': {pferd_daten.index('Hannoveraner')}")
print(f"Anzahl 'Hannoveraner': {pferd_daten.count('Hannoveraner')}")