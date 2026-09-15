class Turnierteilnehmer:
    def __init__(self, reiter, pferd, disziplin):
        self.reiter = reiter
        self.pferd = pferd
        self.disziplin = disziplin
        self.punkte = 0

    def bewerten(self, technik, stil, zeit):
        self.punkte = (technik + stil) * 10 - zeit
        return self.punkte

    def ergebnis(self):
        print(f"🏇 {self.reiter} auf {self.pferd} | {self.disziplin} | {self.punkte} Punkte")

t1 = Turnierteilnehmer("Lisa", "Thunder", "Dressur")
t2 = Turnierteilnehmer("Tom", "Luna", "Springen")
t3 = Turnierteilnehmer("Sarah", "Storm", "Dressur")

t1.bewerten(9, 8, 5)
t2.bewerten(7, 9, 3)
t3.bewerten(10, 10, 8)

teilnehmer = [t1, t2, t3]
teilnehmer.sort(key=lambda t: t.punkte, reverse=True)
print("=== Turnierergebnis ===")
for i, t in enumerate(teilnehmer, 1):
    print(f"  {i}. ", end="")
    t.ergebnis()

print()
print("🎉 Herausforderung abgeschlossen!")
print("🏆 Du hast die Meisterreiterin besiegt!")
print("⭐ Titel erhalten: Pferdeflüsterer")