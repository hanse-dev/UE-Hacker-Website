schiff = "Enterprise"
crew = 150

# f-String – Variable direkt im Text
print(f"Schiff: {schiff}, Crew: {crew}")

# type() – Typ prüfen
print(type(schiff))   # <class 'str'>
print(type(crew))     # <class 'int'>

# len() – Länge
print(len(schiff))    # 10

# String-Methoden
print(schiff.upper()) # ENTERPRISE
print(schiff.lower()) # enterprise
