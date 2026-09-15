# Lösungsvorschlag Boss-Quest 1 – Das Gilden-System

# Schritt 1: Basis-Klasse
class Mitglied:
    def __init__(self, name, rang):
        self.name = name
        self.rang = rang

    def rechte_anzeigen(self):
        print(f"{self.name} ({self.rang}): Grundlegende Gilden-Rechte")

    def __str__(self):
        return f"[{self.rang}] {self.name}"

# Schritt 2: Spezialisierungen
class Lehrling(Mitglied):
    def __init__(self, name):
        super().__init__(name, "Lehrling")

    def rechte_anzeigen(self):
        print(f"{self.name} ({self.rang}): Darf die Bibliothek nutzen und an einfachen Missionen teilnehmen.")

class Geselle(Mitglied):
    def __init__(self, name):
        super().__init__(name, "Geselle")

    def rechte_anzeigen(self):
        print(f"{self.name} ({self.rang}): Darf Missionen auswählen, Lehrlinge ausbilden und das Lager nutzen.")

class Meister(Mitglied):
    def __init__(self, name):
        super().__init__(name, "Meister")

    def rechte_anzeigen(self):
        print(f"{self.name} ({self.rang}): Volle Rechte – Missionen erstellen, Aufnahmen entscheiden, Schatz verwalten.")

# Schritt 3: Polymorphismus in Aktion
gilde = [
    Lehrling("Finn"),
    Geselle("Rowan"),
    Meister("Seraphina")
]

print("=== GILDEN-MITGLIEDER ===")
for mitglied in gilde:
    print(mitglied)           # nutzt __str__
    mitglied.rechte_anzeigen()
    print()