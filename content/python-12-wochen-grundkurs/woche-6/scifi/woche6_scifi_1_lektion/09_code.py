# Beispiel 3: Listen kombinieren
schiffe = ["Nebula-Explorer", "Star-Fighter"]
crew = ["Captain Alex", "Dr. Zara"]
missionen = ["Forschung", "Verteidigung", "Erforschung"]

print("=== Listen kombinieren ===")
print(f"Schiffe: {schiffe}")
print(f"Crew: {crew}")
print(f"Missionen: {missionen}")

# Mit + Operator kombinieren
alle = schiffe + crew + missionen
print(f"Alles kombiniert: {alle}")

# Mit extend() eine Liste zur anderen hinzufügen
schiffe.extend(crew)
print(f"Schiffe erweitert: {schiffe}")