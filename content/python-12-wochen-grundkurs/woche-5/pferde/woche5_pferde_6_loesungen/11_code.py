import random

# Schritt 1 – Begrüßungs-Training
def begruesse_pferd():
    print("Hallo, schönes Pferd! Bereit fürs Training?")
    print("Heute wird ein großartiger Trainingstag!")

begruesse_pferd()
begruesse_pferd()

# Schritt 2 – Trainings-Intensität berechnen
def berechne_intensitaet(level, dauer):
    return level * dauer * 5

# Schritt 3 – Trainings-Möglichkeit prüfen
def ist_training_moeglich(energie):
    return energie >= 50

# Schritt 4 – Haupt-Block
pferd_level = 4
dauer = 3
energie = 75

intensitaet = berechne_intensitaet(pferd_level, dauer)
print(f"Trainingsintensität: {intensitaet}")

if ist_training_moeglich(energie):
    print(f"Training möglich! Energie: {energie}")
else:
    print("Pferd braucht eine Pause.")

# Bonus – zufällige Trainingsart
def generiere_training():
    arten = ["Dressur", "Springen", "Gelände", "Galoppieren", "Trabrennen"]
    return random.choice(arten)

print(f"Heutige Trainingsart: {generiere_training()}")