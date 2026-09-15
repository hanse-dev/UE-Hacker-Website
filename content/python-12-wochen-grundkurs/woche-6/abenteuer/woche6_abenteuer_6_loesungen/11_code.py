# Schritt 1 – Schatzliste anlegen
schaetze = ["Golddukaten", "Rubinring", "Smaragdkette", "Silberpokal", "Elfenstaub"]
print("Schatzliste:", schaetze)

# Schritt 2 – Schätze ergänzen
schaetze.append("Drachenschuppe")
schaetze.append("Feenflügel")
schaetze.append("Mondstein")
schaetze.insert(0, "Legendäres Schwert")
print("Nach Ergänzung:", schaetze)

# Schritt 3 – Schatz entfernen und Position finden
schaetze.remove("Elfenstaub")
position = schaetze.index("Rubinring")
print("Nach Entfernung:", schaetze)
print(f"Position von Rubinring: {position}")

# Schritt 4 – Sortieren und Ausgabe
schaetze.sort()
print("Sortiert:", schaetze)
print(f"Anzahl Schätze: {len(schaetze)}")

# Bonus – verschachtelte Liste
schatz_details = [
    ["Golddukaten", 500, "selten"],
    ["Rubinring", 300, "sehr selten"],
    ["Mondstein", 150, "häufig"]
]
print("\nSchatz-Details:")
for schatz in schatz_details:
    print(f"  {schatz[0]}: {schatz[1]} Gold ({schatz[2]})")