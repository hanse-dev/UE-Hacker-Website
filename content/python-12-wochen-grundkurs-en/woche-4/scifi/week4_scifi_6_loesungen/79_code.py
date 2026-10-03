fuel = 100
shield = 60
distance = 0
while fuel > 0 and shield > 0:
    distance += 1
    fuel -= 20
    shield -= 8
print(f"Tunnel ended after {distance} portals")
if fuel <= 0:
    print("Reason: out of fuel")
