# Beispiel: Das Orakel befragen und die Antwort umwandeln
# (lokal ausführen – in statischen Umgebungen ggf. kommentieren)

name = input("Wie heißt dein Held? ")
level_str = input("Welches Level hat er? ")
level = int(level_str)   # Feuer -> Erde (str -> int)

print(f"Willkommen, {name}!")
print(f"{name} ist auf Level {level}.")
print(f"In 5 Levels erreichst du Level {level + 5}.")
