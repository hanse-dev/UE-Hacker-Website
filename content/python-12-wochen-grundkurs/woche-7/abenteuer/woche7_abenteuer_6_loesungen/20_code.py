import random
import string

# Schritt 1: Glücks-Rune aus dem Namen
name = input("Dein Name: ")
gluecks_rune = "".join(random.choice(string.ascii_uppercase) for _ in range(len(name)))
print(f"\nDeine Glücks-Rune: {gluecks_rune}")

# Schritt 2: Prophezeiung
prophezeiungen = [
    "Ein unerwartetes Abenteuer erwartet dich.",
    "Die Weisheit der Alten wird dich führen.",
    "Ein neuer Freund erscheint auf deinem Weg.",
    "Große Stärke liegt verborgen in dir.",
    "Das Schicksal lächelt dir heute.",
    "Mut wird dir Türen öffnen, die verschlossen schienen.",
]
prophezeiung = random.choice(prophezeiungen)

# Schritt 3: Horoskop
print("\n=== DEIN MAGISCHES HOROSKOP ===")
print(f"Name:         {name}")
print(f"Glücks-Rune:  {gluecks_rune}")
print(f"Prophezeiung: {prophezeiung}")

# Bonus: Wahrscheinlichkeit
wahrscheinlichkeit = round(100 / len(prophezeiungen), 1)
print(f"\nWahrscheinlichkeit dieser Prophezeiung: {wahrscheinlichkeit}%")
