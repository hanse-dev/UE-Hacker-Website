import random

distance = 0
energy = 100

while True:
    portal_energy = random.randint(5, 20)
    energy -= portal_energy
    distance += 1
    print(f"Portal {distance}: -{portal_energy} energy (remaining: {energy})")

    if energy <= 0:
        print(f"Energy depleted after {distance} portals!")
        break
    if distance >= 10:
        print(f"Tunnel exit reached! {distance} portals passed.")
        break

print()
print("🎉 Final challenge complete!")
print("🏆 You have defeated the endless time loop!")
print("⭐ Title unlocked: Master of Time Cycles")