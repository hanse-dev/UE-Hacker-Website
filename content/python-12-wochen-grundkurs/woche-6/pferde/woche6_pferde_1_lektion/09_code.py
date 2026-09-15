# Beispiel 3: Listen kombinieren
pferde = ["Thunder", "Luna", "Storm"]
reiter = ["Anna", "Max", "Sarah"]
trainings = ["Dressur", "Springen", "Western"]

print("=== Listen kombinieren ===")
print(f"Pferde: {pferde}")
print(f"Reiter: {reiter}")
print(f"Trainings: {trainings}")

# Mit + Operator kombinieren
alle = pferde + reiter + trainings
print(f"Alles kombiniert: {alle}")

# Mit extend() eine Liste zur anderen hinzufügen
pferde.extend(reiter)
print(f"Pferde erweitert: {pferde}")