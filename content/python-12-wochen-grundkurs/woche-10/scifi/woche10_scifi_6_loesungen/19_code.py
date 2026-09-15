class CrewMitglied:
    def __init__(self, name, rang, spezialgebiet):
        self.name = name
        self.rang = rang
        self.spezialgebiet = spezialgebiet

    def vorstellen(self):
        print(f"👤 {self.name} | {self.rang} | Spezialität: {self.spezialgebiet}")

    def einsatz(self, mission):
        print(f"{self.name} übernimmt Einsatz: {mission}")

class Crew:
    def __init__(self):
        self.mitglieder = []

    def hinzufuegen(self, mitglied):
        self.mitglieder.append(mitglied)

    def zeige_alle(self):
        print(f"\n=== Crew ({len(self.mitglieder)} Mitglieder) ===")
        for m in self.mitglieder:
            m.vorstellen()

crew = Crew()
crew.hinzufuegen(CrewMitglied("Zara", "Kapitänin", "Navigation"))
crew.hinzufuegen(CrewMitglied("Orion", "Arzt", "Xenobiologie"))
crew.hinzufuegen(CrewMitglied("Maya", "Ingenieurin", "Antriebssysteme"))
crew.zeige_alle()
crew.mitglieder[0].einsatz("Erkundung Sektor 7")