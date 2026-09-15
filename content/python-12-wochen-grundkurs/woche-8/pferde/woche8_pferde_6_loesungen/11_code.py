# Schritt 1: Pferde-Stallkarte anlegen
pferd = {
    "name": "Thunder",
    "rasse": "Hannoveraner",
    "alter": 7,
    "groesse": 168  # Stockmaß in cm
}
print("Pferde-Stallkarte:")
print(pferd)

# Schritt 2: Werte ändern und ergänzen
pferd["alter"] = 8
pferd["besitzer"] = "Lena Müller"
print(f"\nNach Update: Alter {pferd['alter']}, Besitzer {pferd['besitzer']}")

# Schritt 3: Pferde-Liste aus Dictionaries
pferde_liste = [
    {"name": "Thunder", "rasse": "Hannoveraner", "alter": 8},
    {"name": "Luna", "rasse": "Isländer", "alter": 5},
    {"name": "Blitz", "rasse": "Araber", "alter": 4}
]
print(f"\nPferde-Liste: {pferde_liste}")
print(f"Erstes Pferd: {pferde_liste[0]['name']}")

# Schritt 4: Zugriff und Ausgabe
p_name = pferd["name"]
p_rasse = pferd.get("rasse")
print(f"\nPferd: {p_name}, Rasse: {p_rasse}, Alter: {pferd['alter']}")

# Bonus: Verschachteltes Dictionary
pferd["gesundheit"] = {"impfung": "aktuell", "huf": "gepflegt", "zahnarzt": "2025"}
print(f"Huf-Status: {pferd['gesundheit']['huf']}")