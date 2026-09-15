import random

distanz = 0
energie = 100

while True:
    portal_energie = random.randint(5, 20)
    energie -= portal_energie
    distanz += 1
    print(f"Portal {distanz}: -{portal_energie} Energie (verbleibend: {energie})")

    if energie <= 0:
        print(f"Energie erschöpft nach {distanz} Portalen!")
        break
    if distanz >= 10:
        print(f"Tunnel-Ende erreicht! {distanz} Portale durchflogen.")
        break

print()
print("🎉 Finale Herausforderung abgeschlossen!")
print("🏆 Du hast den unendlichen Zeit-Loop besiegt!")
print("⭐ Titel erhalten: Meister der Zeit-Zyklen")