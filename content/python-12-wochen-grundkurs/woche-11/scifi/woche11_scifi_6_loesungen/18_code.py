# Lösungsvorschlag Boss-Quest 1 – Die Rang-Hierarchie

# Schritt 1: Basis-Klasse
class Besatzungsmitglied:
    def __init__(self, name, rang):
        self.name = name
        self.rang = rang

    def befugnisse_anzeigen(self):
        print(f"{self.name} ({self.rang}): Grundlegende Flottenrechte.")

    def __str__(self):
        return f"[{self.rang}] {self.name}"

# Schritt 2: Ränge
class Kadett(Besatzungsmitglied):
    def __init__(self, name):
        super().__init__(name, "Kadett")

    def befugnisse_anzeigen(self):
        print(f"{self.name} ({self.rang}): Zugang zu Trainingsräumen und Schlafsälen. Keine Waffenzugänge.")

class Offizier(Besatzungsmitglied):
    def __init__(self, name):
        super().__init__(name, "Offizier")

    def befugnisse_anzeigen(self):
        print(f"{self.name} ({self.rang}): Zugang zur Brücke, Waffenkammer und Kommandoräumen.")

class Kapitaen(Besatzungsmitglied):
    def __init__(self, name):
        super().__init__(name, "Kapitän")

    def befugnisse_anzeigen(self):
        print(f"{self.name} ({self.rang}): Volle Schiffskontrolle – Kurssetzung, Kampfbefehle, Notfallprotokolle.")

# Schritt 3: Briefing
crew = [
    Kadett("Nova"),
    Offizier("Vega"),
    Kapitaen("Commander Zara")
]

print("=== FLOTTEN-BRIEFING ===")
for mitglied in crew:
    print(mitglied)                  # __str__
    mitglied.befugnisse_anzeigen()
    print()