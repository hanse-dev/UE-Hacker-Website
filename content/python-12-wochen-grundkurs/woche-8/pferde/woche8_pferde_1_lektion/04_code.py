# Beispiel 2: Auf Stallkarten zugreifen
pferd = {
    "name": "Thunder",
    "rasse": "Hannoveraner",
    "alter": 8,
    "groesse": 1.72
}

print("=== Pferde-Zugriff ===")
print(f"Pferde-Name: {pferd['name']}")
print(f"Rasse: {pferd['rasse']}")
print(f"Alter: {pferd['alter']} Jahre")
print(f"Größe: {pferd['groesse']} m")

# Mit get() Methode (sicherer)
print(f"\nMit get(): {pferd.get('name')}")
print(f"Nicht existierend: {pferd.get('geschlecht', 'Unbekannt')}")