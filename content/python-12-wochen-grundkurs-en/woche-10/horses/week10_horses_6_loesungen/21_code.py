class TournamentParticipant:
    def __init__(self, rider, horse, discipline):
        self.rider = rider
        self.horse = horse
        self.discipline = discipline
        self.points = 0

    def score(self, technique, style, time):
        self.points = (technique + style) * 10 - time
        return self.points

    def result(self):
        print(f"🏇 {self.rider} on {self.horse} | {self.discipline} | {self.points} points")

t1 = TournamentParticipant("Lisa", "Thunder", "Dressage")
t2 = TournamentParticipant("Tom", "Luna", "Jumping")
t3 = TournamentParticipant("Sarah", "Storm", "Dressage")

t1.score(9, 8, 5)
t2.score(7, 9, 3)
t3.score(10, 10, 8)

participants = [t1, t2, t3]
participants.sort(key=lambda t: t.points, reverse=True)
print("=== Tournament Result ===")
for i, t in enumerate(participants, 1):
    print(f"  {i}. ", end="")
    t.result()

print()
print("🎉 Challenge completed!")
print("🏆 You have defeated the Master Rider!")
print("⭐ Title earned: Horse Whisperer")