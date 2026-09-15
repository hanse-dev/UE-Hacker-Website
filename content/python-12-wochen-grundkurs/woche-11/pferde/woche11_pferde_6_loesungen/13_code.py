# Lösungsvorschlag Mission 2 – Das polymorphe Training

# Schritt 1: Drei Trainings-Klassen
class Dressur:
    def __init__(self, name):
        self.name = name

    def training(self):
        print(f"[{self.name}] Piaffe üben – Trab auf der Stelle, elegant und präzise!")

class Springen:
    def __init__(self, name):
        self.name = name

    def training(self):
        print(f"[{self.name}] Parcours springen – Hindernisse in der richtigen Reihenfolge!")

class Western:
    def __init__(self, name):
        self.name = name

    def training(self):
        print(f"[{self.name}] Slalom reiten – locker und gelassen zwischen den Stangen!")

# Schritt 2: Polymorphe Funktion
def trainiere_pferd(pferd_name, training):
    print(f"Pferd '{pferd_name}' nimmt am Training teil:")
    training.training()

# Schritt 3: Alle Trainings testen
dressur_stunde = Dressur("Dressur")
spring_kurs = Springen("Springen")
western_kurs = Western("Western")

trainiere_pferd("Valencia", dressur_stunde)
trainiere_pferd("Falke", spring_kurs)
trainiere_pferd("Navajo", western_kurs)

# Bonus: Trainer-Fabrik
def trainer_fabrik(typ, name):
    if typ == "dressur":
        return Dressur(name)
    elif typ == "springen":
        return Springen(name)
    elif typ == "western":
        return Western(name)
    else:
        print(f"Unbekannte Trainingsart: {typ}")
        return None

print()
neues_training = trainer_fabrik("springen", "Fortgeschrittenes Springen")
trainiere_pferd("Champion", neues_training)