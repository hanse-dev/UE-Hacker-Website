# Boss-Quest 3: Das Monster-Bestiarium

# Schritt 1: Monster-Klasse
class Monster:
    def __init__(self, name, typ, lebenspunkte, angriffskraft):
        self.name = name
        self.typ = typ
        self.lebenspunkte = lebenspunkte
        self.angriffskraft = angriffskraft

    # Schritt 2: Kampf-Methode
    def angreifen(self, ziel):
        schaden = self.angriffskraft
        ziel.lebenspunkte -= schaden
        print(f"{self.name} greift {ziel.name} an! -{schaden} LP. {ziel.name} hat noch {ziel.lebenspunkte} LP.")

    # Bonus: heilen-Methode
    def heilen(self, menge):
        self.lebenspunkte += menge
        print(f"{self.name} heilt sich um {menge} LP. Aktuelle LP: {self.lebenspunkte}")

    def ist_besiegt(self):
        return self.lebenspunkte <= 0

# Schritt 3: Bestiarium – Monster gegeneinander
goblin = Monster("Grumk", "Goblin", 50, 10)
troll = Monster("Ugrak", "Troll", 120, 25)
drache = Monster("Smaug", "Drache", 200, 40)

monster_liste = [goblin, troll, drache]

print("=== Bestiarium ===")
for m in monster_liste:
    print(f"[{m.typ}] {m.name}: {m.lebenspunkte} LP, {m.angriffskraft} Angriff")

print("\n=== Kampf: Goblin vs. Troll ===")
goblin.angreifen(troll)
troll.angreifen(goblin)
troll.angreifen(goblin)

if goblin.ist_besiegt():
    print(f"{goblin.name} wurde besiegt!")
    print(f"Sieger: {troll.name}")

# Bonus: Heilen
print("\n=== Drache heilt sich ===")
drache.heilen(50)