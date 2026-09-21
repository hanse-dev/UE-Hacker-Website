import random

def wuerfle_faehigkeit():
    return random.choice(["Trab", "Galopp", "Sprung"])

alle_gueltig = True
for i in range(20):
    if wuerfle_faehigkeit() not in ["Trab", "Galopp", "Sprung"]:
        alle_gueltig = False
print(f"Alle gültig: {alle_gueltig}")
